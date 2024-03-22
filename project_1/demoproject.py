import hashlib  # For hashing passwords

# Dummy database to store user data (for demonstration purposes)
users_db = {}

def register(username, password):
    if username in users_db:
        print("Username already exists. Please choose a different username.")
        return False
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users_db[username] = hashed_password
    print("Account created successfully. You can now log in.")
    return True

def login(username, password):
    if username not in users_db:
        print("User not found. Please register first.")
        return False
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if users_db[username] == hashed_password:
        print("Login successful.")
        return True
    else:
        print("Incorrect password. Please try again.")
        return False

# Example usage
register("alice", "pass123")
login("alice", "pass123")
login("bob", "password")
