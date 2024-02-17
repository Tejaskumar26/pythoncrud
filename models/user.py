from config.db import db
import uuid 

class User(db.Model):
    id = db.Column(db.Uuid, primary_key=True, default=str(uuid.uuid4()))
    user_name = db.Column(db.String(90), unique=True, nullable=False)
    phone_number = db.Column(db.String, unique=True)
    email = db.Column(db.String(90), unique=True, nullable=False)
    deleted = db.Column(db.Boolean, default=False)  

    posts = db.relationship('Post', backref='author', lazy=True)


def __init__(self, user_name, phone_number, email):
    self.user_name = user_name
    self.phone_number = phone_number
    self.email = email
    self.deleted = False