'''username & password setup PJ 1'''
import hashlib # for hashing passwords 
# database to store user data (for practice)

users_db = {}
def register(username, password):
    if username in users_db:
        print("Username already exists. Please choose a different username.")
        return False

    hash_password = hashlib.sha256(password.encode()).hexdigest()
    print("Account created successfully. You can now log in")
    return True
def login(username, password):
    if username not in users_db:
        print("User not found. Please register first .")
        return False

