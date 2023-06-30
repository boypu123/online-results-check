from flask import Flask, request
from flask_cors import CORS, cross_origin

# Initialisation
app = Flask(__name__)
CORS(app, origins="http://localhost:5173")
# The login method to handle login
@app.route('/login', methods = ['POST'])
def login():
    candidate_number = request.json['candidateNumber']
    password = request.json['password']
    



if __name__ == '__main__':
    app.run(debug=True)