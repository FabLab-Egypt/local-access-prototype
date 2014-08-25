# -*- charset= utf-8 -*-

from flask import Flask
app = Flask(__name__)


@app.route("/M/<uid>")
def member_login(uid): #
''':uid: members RFID'''
    pass

@app.route("/V/<uid>")
def visitor_login(uid):
''':uid: visitor tooken, ie: mobile number'''
    pass

@app.route("/", ['get', 'post'])
def visitor_resigtration():
''':uid: visitor tooken, ie: mobile number'''
    pass

# DB stuff

def db_get():
    pass

def db_set():
    pass


if __name__ == '__main__':
    app.run(
        port=3000,
        debug=True,
    )
