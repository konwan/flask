#!/usr/bin/env python

import os
from flask import Flask, make_response, jsonify, abort, g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JWT

# jsonify parse dict to json

app = Flask(__name__)
auth = HTTPBasicAuth()
authtk = HTTPTokenAuth(scheme='Token')

# ----------------------------  [need to enter ac and pw]  --------------------------------
users = { "cindy": "hello", "jlin": "bye" }

# overwrite this method to check pw
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/loginwithpw')
@auth.login_required
def loginpw():
    return "Hi, %s!" % auth.username()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found~~~'}), 404)


# ----------------------------  [check token]  --------------------------------

# app.config['SECRET_KEY']
secret_key = os.urandom(32)
jwt = JWT(secret_key, expires_in=3600)

checkdata={}
tokens = {}
users = {"cindy":"hi" , "jlin":"yo"}
current_user = None

for i in users :
    token = jwt.dumps({'id': i, 'pw': users[i]})
    tokens[i] = token
    checkdata[i] = jwt.loads(token)
    # print("[{}]    token is {}".format(i, token))

# print(tokens)
# print(checkdata)


@authtk.verify_token
def verify_token(token):
    for u in tokens:
        data = jwt.loads(tokens[u])
        current_user = data['id']
 
        if current_user is not None:
            print("welcome {} login ".format(current_user))
            g.current_user = current_user
            return True
    return False


@app.route('/logintoken')
@authtk.login_required
def logintoken():
    return "Yo yo yo ~~~~~, %s!" % g.current_user


if __name__ == '__main__':
    app.run()
