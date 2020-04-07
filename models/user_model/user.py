from database.db import db,ma
from flask_restful import Resource
from models.store_model.store import Store
from models.store_model.store_relation import StoreRelation

#setting up User Info
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String, nullable=True,unique=True)
    Address = db.Column(db.String, nullable=True)
    Address1 = db.Column(db.String, nullable=True)
    City = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True,unique=False)



class UserInfoSchema(ma.ModelSchema):
    class Meta():
        model = UserInfo
        load_instance = True

#setting up User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    fullname = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_info = db.relationship('UserInfo',backref='user',lazy=True)
    my_stores = db.relationship('Store', backref='user',lazy=True)
    store_dropped=db.relationship('StoreRelation', backref='user',lazy=True)


class UserSchema(ma.ModelSchema):
    class Meta():
        model = User
        load_instance = True
