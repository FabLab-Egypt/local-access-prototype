#!/usr/bin/env python3
# -*- charset= utf-8 -*-

from flask import Flask, request
app = Flask(__name__)


@app.route("/M/<uid>")
def member_login(uid): #
    ''':uid: members RFID'''
    return 'member_login'

@app.route("/V/<uid>")
def visitor_login(uid):
    ''':uid: visitor tooken, ie: mobile number'''
    return 'visitor_login'

@app.route("/", methods=['get', 'post'])
def visitor_resigtration():
    ''':uid: visitor tooken, ie: mobile number'''
    if request.method == 'POST':
        return 'visitor_resigtration [POST]'
    else:
        return 'visitor_resigtration [GET]'
    return 'visitor_resigtration (ERROR)'

# DB stuff

def db_get():
    pass

def db_set():
    pass


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=3000,
        debug=True,
    )
