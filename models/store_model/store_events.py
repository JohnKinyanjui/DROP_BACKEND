from flask import  request
from flask_restful import Api,Resource
from database.db import db
from models.store_model.store import Store,StoreSchema
from models.store_model.store_relation import StoreRelation,StoreRelationSchema
from flask_jwt_extended import (
    JWTManager, jwt_optional, create_access_token,
    get_jwt_identity,jwt_required
)


#Schema
single_store = StoreSchema()
many_stores = StoreSchema(many= True)

drops = StoreRelationSchema(many=True)
#show all stores
class AllStores(Resource):
    def get(self):
        store_query = Store.query.all()
        stores = many_stores.dump(store_query)
        return {"stores":stores}

#Add a new Store
class AddStore(Resource):
    def post(self,id):
        data = request.json
        store_name = data['store_name']
        store_cover = data['store_cover']
        store_photo = data['store_photo']
        store_description = data['store_description']
        owner_id = id
        new_store = Store(store_name=store_name,store_cover=store_cover,store_photo=store_photo,store_description=store_description,owner_id=owner_id)
        db.session.add(new_store)
        db.session.commit()
        return {"message":"Success"}


class AddDrop(Resource):
    def post(self):
        data = request.json
        user_id = data['user_id']
        store_id = data['store_id']
        new_drop = StoreRelation(user_id=user_id,store_id=store_id)
        db.session.add(new_drop)
        db.session.commit()
        return {"message":"Drop Added"}

#All Drops
class Drops(Resource):
    def get(self):
        drops_S = StoreRelationSchema(many=True)
        drop_query = StoreRelation.query.all()
        drops = drops_S.dump(drop_query)
        return {"drop":drops}


