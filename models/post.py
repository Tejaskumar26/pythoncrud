from config.db import db
import uuid 

class Post(db.Model):
    id = db.Column(db.Uuid, primary_key=True, default=str(uuid.uuid4()))
    # user_id = db.Column(db.Uuid, nullable=True)
    user_id = db.Column(db.Uuid, db.ForeignKey('user.id'))
    title = db.Column(db.String, unique=True)
    description = db.Column(db.String(90), unique=True, nullable=False)
    deleted = db.Column(db.Boolean, default=False)


def __init__(self, user_id, title, description):
    self.user_id = user_id
    self.title = title
    self.description = description
    self.deleted = False