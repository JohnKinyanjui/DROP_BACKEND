from database.db import db,ma
from flask_restful import Resource
from flask import request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from models.user_model.user import User,UserSchema,UserInfo,UserInfoSchema



#User Schema
single_user = UserSchema()
many_users = UserSchema(many=True)

#UserInfo Schema
single_user_info = UserInfoSchema() 
many_users_info = UserInfoSchema(many=True)

#Getting All Users
class AllUser(Resource):
    def get(self):
        users_query = User.query.all()
        users = many_users.dump(users_query)
        return {"users":users}

#Getting All User Info
class AllUserInfo(Resource):
    def get(self):
        users_info_query = UserInfo.query.all()
        users_info = many_users_info.dump(users_info_query)
        return {"user_info":users_info}

#Adding User
class AddUser(Resource):
    def post(self):
        users = User.query.all()
        data = request.json
        username = data['username']
        fullname = data['fullname']
        gender = data['gender']
        password = data['password']
        #users query
        #many_userss = UserSchema(many=True)
       # users_query = User.query.all()
        #users = many_userss.dump(users_query)
        #for users in single_user :
            #if single_user['username'] == username:
                #return {"message":"username already taken"}
        #users saving        
        new_user = User(username = username,fullname=fullname,gender=gender,password=password) 
        db.session.add(new_user)
        db.session.commit() 
        return {"message":"User Added"} 
        
#Adding User Info
class AddNewUserInfo(Resource):
    def post(self,id):
        data = request.json
        phone_number = data['phone_number']
        email = data['email']
        address = data['Address']
        address1=data['Address1']
        City=data['City']
        user_id=id
        #users query
        many_userss = UserSchema(many=True)
        users_query = User.query.all()
        users = many_userss.dump(users_query)
        for users in single_user :
            if single_user['email'] == email:
                return {"message":"Email already used"}
        #saving data        
        new_user_info = UserInfo(phone_number=phone_number,email=email,Address=address,Address1=address1,City=City,user_id=id)
        db.session.add(new_user_info)
        db.session.commit()
        return {"message":"User Info Updated"}