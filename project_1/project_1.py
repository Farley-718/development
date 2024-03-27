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