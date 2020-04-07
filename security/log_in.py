from models.user_model.user import User,UserSchema
from flask_restful import Api,Resource
from flask import request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity,jwt_refresh_token_required
)


class LogIn(Resource):
    def post(self):
        data = request.json
        username = data['username']
        password = data['password']
        many_users = UserSchema(many=True)
        users_query = User.query.all()
        users = many_users.dump(users_query)
        for user in users :
            if user['username'] == username and user['password'] == password:
                usr = User(username = username) 
                access_token = create_access_token(identity=username)
                
                return {
                    "access_token":access_token,
                    
                }
        return {"message":"Email and Password do not match"}         


class Refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        return {"access_token": create_access_token(indentity=current_user)}

class protected(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return {"username":current_user}





