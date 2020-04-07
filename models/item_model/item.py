from database.db import db,ma

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    item_image = db.Column(db.String,nullable=True)
    item_cover = db.Column(db.String, nullable=True)
    name = db.Column(db.String(20),nullable=False)
    detail = db.Column(db.String(300),nullable=True) 
    date_Added = db.Column(db.String,nullable=True)
    cost = db.Column(db.Integer, nullable=False)
    number_of_items = db.Column(db.Integer, nullable=False)



class ItemSchem(ma.ModelSchema):
    class Meta():
        model = Item
 
