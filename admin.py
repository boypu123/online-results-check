from pymongo import MongoClient
import hashlib

client = MongoClient("localhost", 27017)

db = client.results_query

password = hashlib.sha256(b'123456').hexdigest()
db.login.insert_one({'username': 'testaccount.001', 'password':password})