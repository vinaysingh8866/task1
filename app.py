from models.User import User, getUsers, addUser
from flask import Flask, request, jsonify
import re
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///socialMedia.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
User = User(db)
#print(getUsers(User))

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
        addUser(db,User, uname, email, upassword)
        return jsonify({"success": True})
    except Exception as e:
        print(e)
        return jsonify({"error": "Invalid Request"})


if __name__ == "__main__":
    app.run(debug=True)
