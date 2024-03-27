def register(users):
    username = input("Please enter a username:")
    password = input("please enter a password: ")
    confirm_password = input("please confirm your password: ")
    if password != confirm_password:
        print("Password do not match , please try again. ")
    elif any(username == u[0] for u in users):
        print("Passwords do not match. Please try again.")
    









def login(users):
    while True :
        username = input("please enter a username: ")
        password = input("please enter password: ")
        for u in users :
            if username == u [0] and password == u[1]:
                return username
            print("username or password is incorrect. please try again !")






  


users = [['johnjay','cba321'],['farley','smart123'],['quan','543smart']]
username = login(users)
print(username,"Has logged in")