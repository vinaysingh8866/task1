def User(db):

    class User(db.Model):
        uid = db.Column(db.Integer,
                    primary_key=True)
        uname = db.Column(db.String(24))
        email = db.Column(db.String(64))
        upassword = db.Column(db.String(64))

        # Constructor
        def __init__(self, uname, email, upassword):
            self.uname = uname
            self.email = email
            self.upassword = upassword

    
    return User

def getUsers(User):
        users = User.query.all()
        return [{"id": i.uid, "username": i.uname, "email": i.email, "password": i.upassword} for i in users]