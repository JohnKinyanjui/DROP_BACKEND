from database.db import db,ma
from models.store_model.store_relation import StoreRelation
from models.item_model.item import Item

#Setting up store
class Store(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String, nullable=False, unique=True)
    store_cover = db.Column(db.String,nullable=True)
    store_photo = db.Column(db.String,nullable=True)
    store_category = db.Column(db.String, nullable=True)
    store_description = db.Column(db.String, nullable=True)
    items = db.relationship('Item', backref = 'store', lazy=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    dropers = db.relationship('StoreRelation', backref='store',lazy=True)

class StoreSchema(ma.ModelSchema):
    class Meta():
        model = Store
 