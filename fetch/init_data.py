from app import *
f"""rom models import *

def add_payee(new_payee):
    the_payee = Payer(payee = new_payee)
    db.session.add(the_payee)
    db.session.commit()
    all_payees = Payer.query.all()
    print(all_payees[0])

def add_user(first_name, surname, email, username, password):
    the_user = User(first_name=first_name, surname=surname, email=email, username=username, password=password)
    db.session.add(the_user)
    db.session.commit()
    all_users = User.query.all()
    print(all_users[0])
"""
#add_user('Megan', 'Maple', 'email@email.com', 'maplem', 'passit')
#add_user('M', 'Mple', 'eml1@email.com', '1map', 'lkjinit')
#add_user('asd', 'Maple', 'il3@email.com', '3maplem', 'lllsit')


#add_payee('DANNON')
#add_payee('UNILEVER')
#add_payee('MILLER COORS')

# unit testing
"""
from flask.ext.testing import TestCase

from myapp import create_app, db

class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return create_app(self)

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()
"""





