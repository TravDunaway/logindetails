
from logindetailsapp import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique=True, index=True)
    username = db.Column(db.String(255), unique=True,index=True)
    password_hash = db.Column(db.String(128))

    times = db.relationship("Time", backref = "user", lazy = True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

class Time(db.Model):

    __tablename__ = "times"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    time = db.Column(db.Integer, unique = False, nullable = False)
    current_location = db.Column(db.Integer, unique = False, nullable = False)
    date = db.Column(db.Integer, unique = False, nullable = False)

    choices = db.relationship("Choice", backref = "time", lazy = True)

class Choice(db.Model):

    __tablename__ = "choices"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    time_id = db.Column(db.Integer, db.ForeignKey("times.id"), unique = False,  nullable = False)
    trip_time = db.Column(db.Integer, unique = False,  nullable = False)
    desination = db.Column(db.Integer, unique = False,  nullable = False)
    


