from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Client(db.Model):
    __tablename__ = 'clients'
    code = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    price = db.Column(db.Float)
    supplier = db.Column(db.String)
