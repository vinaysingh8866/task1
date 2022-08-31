from models.InvalidToken import getInvalidToken
from models.Tweet import addNewTweet, delAddedTweet, getAddedTweets, getTweet, getUserAddedTweets, updateAddedTweet
from models.User import User, getUsers, addUser
from flask import Flask, request, jsonify
import re
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, \
    jwt_refresh_token_required, create_refresh_token, get_raw_jwt
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///socialMedia.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
User = User(db)
Tweet = getTweet(db)
app.config["JWT_SECRET_KEY"] = "test123123Testabcrfggajkshhk"
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]
jwt = JWTManager(app)


InvalidToken = getInvalidToken(db)


@jwt.token_in_blacklist_loader
def check_if_blacklisted_token(decrypted):
    jti = decrypted["jti"]
    return InvalidToken.is_invalid(jti)


@app.route("/api/register", methods=["POST"])
def register():
    try:
        email = request.json["email"]
        email = email.lower()
        upassword = request.json["upassword"]
        uname = request.json["uname"]
        if not (email and upassword and uname):
            return jsonify({"error": "Invalid Requet"})
        users = getUsers(User)
        print(users)
        usersByEmail = list(filter(lambda x: (x["email"] == email), users))
        if len(usersByEmail) == 1:
            return jsonify({"error": "Invalid Request"})

        if not re.match(r"[\w._]{5,}@\w{3,}\.\w{2,4}", email):
            return jsonify({"error": "Invalid email"})
        addUser(db, User, uname, email, upassword)
        return jsonify({"success": True})
    except Exception as e:
        print(e)
        return jsonify({"error": "Invalid Request"})


@app.route("/api/login", methods=["POST"])
def login():
    try:
        upassword = request.json["upassword"]
        email = request.json["email"]
        if email and upassword:
            user = list(filter(
                lambda x: x["email"] == email and upassword == x["upassword"], getUsers(User)))
            if len(user) == 1:
                refresh_token = create_refresh_token(identity=user[0]["id"])
                token = create_access_token(identity=user[0]["id"])
                returnJson = jsonify(
                    {"token": token, "refreshToken": refresh_token})
                return returnJson
            else:
                return jsonify({"error": "Invalid Password"})
        else:
            return jsonify({"error": "Invalid Request"})
    except Exception as e:
        return jsonify({"error": "Invalid Request"})


@app.route("/api/token_test", methods=["POST"])
@jwt_required
def tokenTest():
    return jsonify({"success": True})


@app.route("/api/new_token", methods=["POST"])
@jwt_refresh_token_required
def newToken():
    identity = get_jwt_identity()
    token = create_access_token(identity=identity)
    return jsonify({"token": token})


@app.route("/api/logout/", methods=["POST"])
@jwt_required
def logout():
    jti = get_raw_jwt()["jti"]
    # Make Token Invalid
    try:
        invalid_token = InvalidToken(jti=jti)
        invalid_token.save()
        return jsonify({"success": True})
    except Exception as e:
        print(e)
        return {"error": e.message}


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
