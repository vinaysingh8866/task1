from flask import Blueprint, request, jsonify,current_app
from models.Tweet import addNewTweet, delAddedTweet, getAddedTweets, getUserAddedTweets, updateAddedTweet
from flask_jwt_extended import jwt_required, get_jwt_identity
blueprint_tweet= Blueprint('blueprint_tweet', __name__)
app = current_app


@blueprint_tweet.route("/api/all_tweets")
def getTweets():
    with app.app_context():
        User = current_app.config['user']
        Tweet = current_app.config['tweet']
        return jsonify(getAddedTweets(Tweet, User))


@blueprint_tweet.route("/api/add_tweet", methods=["POST"])
@jwt_required
def addTweet():
    with app.app_context():
        db = current_app.config['db']
        User = current_app.config['user']
        Tweet = current_app.config['tweet']
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


@blueprint_tweet.route("/api/delete_tweet/<tid>", methods=["DELETE"])
@jwt_required
def deleteTweet(tid):
    with app.app_context():
        db = current_app.config['db']
        Tweet = current_app.config['tweet']
        try:
            delAddedTweet(Tweet, db, tid)
            return jsonify({"success": "true"})
        except:
            return jsonify({"error": "Invalid form"})

@blueprint_tweet.route("/api/user_tweets", methods=["POST"])
@jwt_required
def userTweets():
    with app.app_context():
        Tweet = current_app.config['tweet']
        try:
            uid = get_jwt_identity()
            tweets = getUserAddedTweets(Tweet, uid)
            return jsonify(tweets)
        except:
            return jsonify({"error": "Invalid form"})


@blueprint_tweet.route("/api/update_tweet/<tid>", methods=["POST"])
@jwt_required
def updateTweet(tid):
    with app.app_context():
        db = current_app.config['db']
        Tweet = current_app.config['tweet']
        content = request.json["content"]
        try:
            updateAddedTweet(Tweet, db, tid, content)
            return jsonify({"success": "true"})
        except:
            return jsonify({"error": "Invalid form"})