from models.InvalidToken import getInvalidToken
from models.Tweet import addNewTweet, delAddedTweet, getAddedTweets, getTweet, getUserAddedTweets, updateAddedTweet
from models.User import User, getUsers, addUser
from flask import Flask, request, jsonify
import re
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, \
    jwt_refresh_token_required, create_refresh_token, get_raw_jwt
from flask_sqlalchemy import SQLAlchemy
from blueprints.blueprintAuth import blueprint_auth
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///socialMedia.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
User = User(db)
Tweet = getTweet(db)
InvalidToken = getInvalidToken(db)
app.config["user"] = User
app.config["tweet"] = Tweet
app.config["db"] = db
app.config["invalidToken"] = InvalidToken
app.config["JWT_SECRET_KEY"] = "test123123Testabcrfggajkshhk"
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]
jwt = JWTManager(app)



app.register_blueprint(blueprint_auth)

@jwt.token_in_blacklist_loader
def check_if_blacklisted_token(decrypted):
    jti = decrypted["jti"]
    return InvalidToken.is_invalid(jti)

@app.route("/api/all_tweets")
def getTweets():
    return jsonify(getAddedTweets(Tweet, User))


@app.route("/api/add_tweet", methods=["POST"])
@jwt_required
def addTweet():
    try:
        title = request.json["title"]
        content = request.json["content"]
        if not (title and content):
            return jsonify({"error": "Invalid request"})
        uid = get_jwt_identity()
        addNewTweet(Tweet, db, User, title, content, uid)
        return jsonify({"success": "true"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Invalid Request"})


@app.route("/api/delete_tweet/<tid>", methods=["DELETE"])
@jwt_required
def deleteTweet(tid):
    try:
        delAddedTweet(Tweet, db, tid)
        return jsonify({"success": "true"})
    except:
        return jsonify({"error": "Invalid form"})

@app.route("/api/user_tweets", methods=["POST"])
@jwt_required
def userTweets():
    try:
        uid = request.json["uid"]
        tweets = getUserAddedTweets(Tweet, uid)
        return jsonify(tweets)
    except:
        return jsonify({"error": "Invalid form"})


@app.route("/api/update_tweet/<tid>", methods=["POST"])
@jwt_required
def updateTweet(tid):
    content = request.json["content"]
    try:
        updateAddedTweet(Tweet, db, tid, content)
        return jsonify({"success": "true"})
    except:
        return jsonify({"error": "Invalid form"})


if __name__ == "__main__":
    app.run(debug=True)
