from flask import Flask
from view import api
from model import db
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:FPziJgMmc8@localhost:5432/Odoo'
    app.register_blueprint(api)
    db.init_app(app)
    return app
