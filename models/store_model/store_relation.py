from database.db import db,ma


#Setting up relationships store => clients
class StoreRelation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'),nullable=False)         

class StoreRelationSchema(ma.ModelSchema):
    class Meta():
        model = StoreRelation    