import unittest
from view import api
from model import db
from flask import Flask

class MyTestCase(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config['SQLAlchemy_DATABASE_URI'] = 'postgresql://postgres:FPziJgMmc8@localhost:5432/Odoo'
        app.register_blueprint(api)
        self.app = app.test_client()
        db.init_app(app)
    def tearDown(self):
        pass
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_deletion_page(self):
        response = self.app.get('/deletion', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
