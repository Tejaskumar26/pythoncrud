from config.db import db
import uuid 

class Like(db.Model):
    id = db.Column(db.Uuid, primary_key=True, default=str(uuid.uuid4()))
    post_id = db.Column(db.Uuid, nullable=False)
    user_id = db.Column(db.Uuid, nullable=False)
    comments = db.Column(db.String)
    deleted = db.Column(db.Boolean, default=False) 

def __init__(self, user_id, post_id, comments):
    self.user_id = user_id
    self.post_id = post_id
    self.comments = comments
    self.deleted = False