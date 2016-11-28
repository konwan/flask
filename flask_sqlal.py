#!/usr/bin/env python
#coding=UTF-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/data/Desktop/cindy/gomi/flask_ex/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name

"""
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app
"""

@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.create_all()
    
    cindy = User('cindy', 'cindy@cindy.com')
    db.session.add(cindy)

    others = [User('guest1', 'guest1@example.com'),
               User('guest2', 'guest2@example.com'),
               User('guest3', 'guest3@example.com'),
               User('guest4', 'guest4@example.com')]
    db.session.add_all(others)
    db.session.commit()

@app.route('/user')
def users():
    users = User.query.all()
    return "<br>".join(["{0}: {1}".format(user.name, user.email) for user in users])

@app.route('/user/<int:id>')
def user(id):
    user = User.query.filter_by(id=id).one()
    return "{0}: {1}".format(user.name, user.email)

if __name__ == '__main__':
    app.run('127.0.0.1', 5000) 
