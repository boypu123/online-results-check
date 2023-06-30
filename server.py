from flask import Flask, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import jsonify
import logging
import datetime

# Connect to mongoDB database
client = MongoClient("localhost", 27017)
db = client.results_query

# Initialisation
app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# The login method to handle login
@app.route('/login', methods = ['POST'])
def login():

    username = request.json['username']
    password = request.json['password']
    if (db.username.find_one({'username': username, 'password': password})):
        response = jsonify({'passed': True, 'message': 'Your login creditals are correct. Redirecting.'})
        response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5173')
        return response
    else:
        response = jsonify({'passed': False, 'message': 'Your login creditals are incorrect. Try again.'})
        response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5173')
        return response
    



if __name__ == '__main__':
    app.run(debug=True)