from config.db import db
import uuid 

class Employee(db.Model):
    id = db.Column(db.Uuid, primary_key=True, default=str(uuid.uuid4()))
    emp_name = db.Column(db.String(90), nullable=False)
    phone_number = db.Column(db.String, unique=True)
    email = db.Column(db.String(90), unique=True, nullable=False)
    deleted = db.Column(db.Boolean, default=False)


def __init__(self, emp_name, phone_number, email):
    self.emp_name = emp_name
    self.phone_number = phone_number
    self.email = email
    self.deleted = False