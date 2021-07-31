from model import Client,db
def delete_client(code):
    db.session.query(Client).filter(Client.code == code).delete()
    db.session.commit()
def insert_client(code,name,type,price,supplier):
    if Client.query.filter_by(code=code).scalar() is not None:
        delete_client(code)
    client = Client(code=code,name=name,type=type,price=price,supplier=supplier)
    db.session.add(client)
    db.session.commit()
def retrieve_data():
    return Client.query.all()
def fabric_data():
    return Client.query.filter(Client.type == 'fabric').all()
def jeans_data():
    return Client.query.filter(Client.type == 'jeans').all()
def cotton_data():
    return Client.query.filter(Client.type == 'cotton').all()
