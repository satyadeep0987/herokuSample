import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)


@app.route('/')
def get_greeting():
    excited = os.environ['EXCITED']
    greeting = "Hello it sdservices made by be Satyadeep ...... " 
    if excited == 'true': greeting = greeting + "!!!!!"
    return greeting

@app.route('/coolkids')
def be_cool():
    return "Be cool, man, be coooool! You're almost a FSND grad!"



if __name__ == '__main__':
    app.run()