from __future__ import unicode_literals
from enum import unique
from operator import index
from app import db, datetime


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    payee= db.Column(db.String(30), index = True, unique = False)
    points = db.Column(db.Integer, index = True, unique = False)
    timestamp = db.Column(db.DateTime(), index = True, default=datetime.utcnow)

    def __init__(self, payee, points, timestamp):
        self.payee = payee
        self.points = points
        self.timestamp = timestamp
        



"""class Payer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    payee = db.Column(db.String(50), index = True, unique = True)
    transaction = db.relationship('Transaction', backref = 'payer', lazy = 'dynamic', cascade = "all, delete, delete-orphan")

    def __init__(self, payee):
        self.payee = payee
"""


"""class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), index = True, unique = False)
    surname = db.Column(db.String(50), index = True, unique = False)
    email = db.Column(db.String(80), index = True, unique = True)
    username = db.Column(db.String(40), index = True, unique = True)
    password = db.Column(db.String(40), index = True, unique = True)
    transaction = db.relationship('Transaction', backref = 'user', lazy = 'dynamic', cascade = "all, delete, delete-orphan")

    def __init__(self, first_name, surname, email, username, password):
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.username = username
        self.password = password
"""
