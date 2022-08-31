from models.User import getUser


def getTweet(db):
    class Tweet(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        uid = db.Column(db.Integer, db.ForeignKey("user.uid"))
        user = db.relationship('User', foreign_keys=uid)
        title = db.Column(db.String(256))
        content = db.Column(db.String(2048))
    return Tweet

def getAddedTweets(Tweet, User):
    tweets = Tweet.query.all()
    return [{"id": i.id, "title": i.title, "content": i.content, "user": getUser(User, i.uid)} for i in tweets]


def getUserAddedTweets(Tweet,uid):
    tweets = Tweet.query.all()
    print(tweets[0].id)
    return [{"id": item.id, "userid": item.uid, "title": item.title, "content": item.content} for item in
            filter(lambda i: i.uid == uid, tweets)]


def addNewTweet(Tweet,db,User,title, content, uid):
    try:
        user = list(filter(lambda i: i.uid == uid, User.query.all()))[0]
        twt = Tweet(title=title, content=content, user=user)
        db.session.add(twt)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delAddedTweet(Tweet,db,tid):
    try:
        tweet = Tweet.query.get(tid)
        db.session.delete(tweet)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False

def updateAddedTweet(Tweet,db,tid, content):
    try:
        tweet = Tweet.query.get(tid)
        tweet.content = content
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False