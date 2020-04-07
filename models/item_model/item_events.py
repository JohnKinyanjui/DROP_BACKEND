from flask_restful import Api,Resource
from models.item_model.item import Item
from flask import request
from database.db import db,ma

class AddItem(Resource):
    def post(self):
        data = request.json
        store_id = data['store_id']
        item_image = data['item_image']
        item_cover = data['item_cover']
        name = data['name']
        detail = data['detail']
        date_Added = data['date_Added']
        cost = data['cost']
        number_of_items = data['number_of_items']

        new_item = Item(
            store_id = store_id,
            item_image = item_image,
            item_cover =item_cover,
            name = name,
            detail = detail,
            date_Added = date_Added,
            cost = cost,
            number_of_items = number_of_items
        )

        db.session.add(new_item)
        db.session.commit()
        return {"message":"Item Added"}
