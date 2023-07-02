from pymongo import MongoClient

# Connect
client = MongoClient("localhost", 27017)

# Build
db = client["results_query"]

# Create "login"
login_collection = db["login"]

# Create "results"
results_collection = db["results"]

# 打印数据库和集合的信息
print('Success!')
