from pymongo import MongoClient
import logging
from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin

# The basic config of logging
logging.basicConfig(
    filename = 'log.txt',
    format = '%(asctime)s: %(levelname)s - %(message)s'
)
# Connect to mongoDB database
client = MongoClient("localhost", 27017)
db = client.results_query

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

@app.route('/login', methods=['POST', 'OPTIONS'])
def login():
    # Handle CORS
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': 'http://localhost:5173',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return ('', 204, headers)

    # Get username & password
    username = str(request.json['username'])
    password = str(request.json['password'])
    query_details = db.login.find_one({'username': username, 'password': password})
    if (query_details != None):
        response = jsonify({'status': 'OK', 
                            'message': 'Your login creditals are correct. Redirecting.', 
                            'name': query_details['name'],
                            'candidateNum': query_details['candidateNum'],
                            'centre': query_details['centre']})
        # Log into the log
        logging.info('{} have successfully logged in.'.format(query_details['username']))
        return response
    else:
        response = jsonify({'status': 'Blocked', 'message': 'Your login creditals are incorrect. Try again.'})
        # Log into the
        logging.error('A person did not login successfully. The login creditals are incorrect. The username provided is: {}'.format(username))
        return response


CORS(app, origins=["http://localhost:5173"])
@app.route('/results', methods = ['POST','OPTIONS'])
def results():
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': 'http://localhost:5173',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return ('', 204, headers)
    
    username = str(request.json['username'])
    print(username)
    return str(db.results.find_one({'username':username}))




if __name__ == '__main__':
    app.run('localhost', port='5000', debug=True)