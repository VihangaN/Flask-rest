from flask import Flask , request , jsonify
from flask_sqlalchemy import sqlalchemy
from flask_marshmallow import Marshmallow
import os

#init

app = Flask(__name__)

@app.route('/',methods=['get'])
def get():
    return '<h1>Hello Flask </h1>'

@app.route("/data",methods=['get'])
def data():
    return jsonify({'msg':'Hello Flask!'})

#server

if __name__ == '__main__':
    app.run(debug=True)
