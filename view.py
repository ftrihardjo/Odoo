from flask import Blueprint,render_template,request
from controller import *
api = Blueprint('api',__name__)
@api.route('/')
def registration():
    return render_template('registration.html')
@api.route('/deletion')
def deletion():
    return render_template('deletion.html')
@api.route('/delete',methods=['POST'])
def delete():
    code = request.form['code']
    delete_client(code)
    return render_template('deletion.html')
@api.route('/register',methods=['POST'])
def register():
    code = request.form['code']
    name = request.form['name']
    type = request.form['type']
    price = request.form['price']
    supplier = request.form['supplier']
    insert_client(code,name,type,price,supplier)
    return render_template('registration.html')
@api.route('/database')
def display_database():
    return render_template('database.html',data=retrieve_data())
@api.route('/fabric')
def fabric_database():
    return render_template('type.html',data=fabric_data())
@api.route('/jeans')
def jeans_database():
    return render_template('type.html',data=jeans_data())
@api.route('/cotton')
def cotton_database():
    return render_template('type.html',data=cotton_data())
