from multiprocessing import current_process
from urllib import response
from xmlrpc.client import Transport
from app import db, app
from models import Transaction
from flask import current_app, render_template, request, url_for, redirect, jsonify, Flask, abort
from flask_wtf import FlaskForm
from wtforms import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import func



@app.route('/add_points', methods=['POST'])
def add_points():
    if not request.json or not 'payee' in request.json  or not 'points' in request.json:
        abort(400)
    now = datetime.now()
    new_trans = Transaction(
        payee=request.json['payee'], 
        points= request.json['points'], 
        timestamp= request.json.get('timestamp', now ))

    db.session.add(new_trans)
    db.session.commit()
    current_balance = Transaction.query.with_entities(func.sum(Transaction.points).label('Balance')).first().Balance
    response = {
        'Success' : True,
        'balance' : current_balance
    }
    return jsonify(response), 201

@app.route('/spend_points', methods=['POST'])
def spend_points():
    all_trans_date = Transaction.query.order_by(Transaction.timestamp).all()
    if not request.json or not 'points' in request.json:
        abort(400)
    spent_points = {
        'points' : request.json['points']
    }
    spoints = spent_points['points']
    current_balance = Transaction.query.with_entities(func.sum(Transaction.points).label('Balance')).first().Balance
    if spoints <= current_balance:
        dannon = 0
        unilever = 0
        miller_coors = 0
        spending = spoints
        for trans in all_trans_date:
            if spoints > 0:
                if trans.points >= spoints:
                    trans.points = trans.points - spoints
                    if 'dannon' in trans.payee.lower():
                        dannon += spoints
                        spoints = 0
                    if 'unilever' in trans.payee.lower():
                        unilever += spoints
                        spoints = 0
                    if 'miller' in trans.payee.lower():
                        miller_coors += spoints
                        spoints = 0
                elif trans.points < spoints:
                    amount = trans.points
                    spoints = spoints - trans.points
                    trans.points = 0
                    if 'dannon' in trans.payee.lower():
                        dannon += amount
                    if 'unilever' in trans.payee.lower():
                        unilever += amount
                    if 'miller' in trans.payee.lower():
                        miller_coors += amount
        db.session.commit()                
        responible = { 
            'Dannon' : dannon, 
            'Unilever': unilever, 
            'Miller Coors' : miller_coors,
            'All Points Spent': spending
        }
        return jsonify(responible), 201
    else:
        not_valid = 'This account does not have enough points for this purchase'
        return jsonify(not_valid), 201    

@app.route('/balences', methods=['GET'])
def balances():
    all_trans = Transaction.query.all()
    dannon = 0
    unilever = 0
    miller_coors = 0
    current_balance = 0
    for trans in all_trans:
        if 'dannon' in trans.payee.lower():
            dannon += trans.points
            current_balance += trans.points
        if 'unilever' in trans.payee.lower():
            unilever += trans.points
            current_balance += trans.points
        if 'miller' in trans.payee.lower():
            miller_coors += trans.points
            current_balance += trans.points
    balance = { 
        'Dannon' : dannon, 
        'Unilever': unilever, 
        'Miller Coors' : miller_coors,
        'Total Point Balance': current_balance
        }
    return jsonify(balance), 201


