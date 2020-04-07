from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///drop_database.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'

api = Api(app)

#importing models 
from database.db import db

#importing models
from models.user_model.user import User,UserInfo
from models.store_model.store import Store

#create the database
db.create_all()

#importing events
from models.user_model.user_events import AddUser,AddNewUserInfo,AllUser,AllUserInfo
from models.store_model.store_events import AllStores,AddStore,Drops,AddDrop
from models.item_model.item_events import AddItem
from security.token_manager import jwt
from security.log_in import LogIn,Refresh,protected






#get request
api.add_resource(AllUser,'/users')
api.add_resource(AllUserInfo,'/UserInfo')
api.add_resource(AllStores,'/stores')
api.add_resource(Drops,'/drops')


#post request
api.add_resource(AddNewUserInfo,'/addUserInfo/<int:id>')
api.add_resource(AddUser, '/AddUser')
api.add_resource(AddStore,'/AddStore/<int:id>')
api.add_resource(AddDrop,'/AddDrop')
api.add_resource(AddItem, '/AddItem')

#log in request to get token
api.add_resource(LogIn,'/login')
api.add_resource(protected,'/test')
api.add_resource(Refresh,'/refresh_token')
