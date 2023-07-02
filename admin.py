from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.results_query

def add_score(document, qualification):
    # While True - until exit, continue running
    while True:
        temp_subject = input("Enter the name of the subject (or 'exit;' to finish): ")
        if temp_subject == "exit;":
            break
        temp_score = input("Enter the score for that subject: ")
        document['results'][qualification][temp_subject] = temp_score

def add_user(document):
    print("Now we will enter the result entry mode. Enter 'exit;' to finish.")
    # Until exit, continue running
    while True:
        qualification = input("Please input the name of the qualification (or 'exit;' to finish): ")
        if qualification == "exit;":
            break
        document['results'][qualification] = {}
        add_score(document, qualification)

# Welcome
print("Welcome to the admin panel.")
choice = input("Please choose the action you want to perform:\n1) Add User/Change User Details\n2) Remove User\n3) Check User Details\n")

if choice == "1":
    result_document = {'results':{}}
    login_document = {}
    # Series of inputs
    result_document['username'] = input("Please input username of the new user: ")
    if (db.login.find_one({'username': result_document['username']}) != None):
        print("WARNING: This username is already taken. You are changing the user details.")
    login_document['username'] = result_document['username']
    login_document['name'] = input("Please input the name of the candidate: ")
    login_document['candidateNum'] = input("Please input the candidate number of the new user: ")
    login_document['centre'] = input("Please input the centre where candidate took the exam in: ")
    login_document['password'] = input("Please input the password of the new user: ")
    db.login.insert_one(login_document)
    print("Login details added")
    add_user(result_document)
    db.results.insert_one(result_document)
    print("New user added")
elif choice == "2": # Delete users
    remove_username = input("Enter the username of the user you want to remove")
    # Delete in the login database
    db.login.delete_one({'username':remove_username})
    # Delete in the results database
    db.results.delete_one({'username':remove_username})
    print("User Deleted")
elif choice == "3": # Check user details
    query_username = input("Please enter the username of the user you want to check")
    print(db.login.find_one({'username':query_username}))
    print(db.results.find_one({'username':query_username}))
    print("Query complete.")