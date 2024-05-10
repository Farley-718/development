from datetime import datetime

'''Write a program that will take the user's first name, and than the users last name, and print the value to a text file on 2 separate lines'''
# firstname = input('first name:')
# lastname = input("Last Name:")

# f = open('my_output.txt', 'w') # we are opening a new file
# f.write(f'{firstname}\n{lastname}')
# f.close()

#with open 





''' Write a function called print_even_numbers that will take in a list of integer values and will extract the even numbers from that list and write to a text file let's try different parameters in our open function x, a, w'''

def find_even_numbers(our_list):
    output_list = []
    for m in our_list:
        if m % 2 == 0:
            output_list.append(m)
    with open('output.txt', 'w') as output:
        for o in output_list:
            o = str(o)
            output.writelines(o)
    
    print('file printed Successfully')

my_list = [1,2,3,4,5,6,7,12,14,15,21,22]

find_even_numbers(my_list)
 

''' Lets read in the song lyrics and put it into a list, but before we do, lets look at other options we have to read files in'''
# with open('time_to_say_goodbye.txt','r') as lyrics:
#     my_paragraph = lyrics.read()# will read in everthing
#     my_line = lyrics.readline()
#     lyric_list = lyrics.readlines()

# print(my_paragraph)
# print(my_line)
# print(lyric_list)



''' Bank account class 
Create the bank account class per the specifications in the powerpoint.  
'''

class BankAccount: 
    def __init__(self,customer_name :str, acct_num: int , date: str, balance: float):
        self.customer_name= customer_name
        self.acct_num = acct_num
        self.date= date
        self.balance = balance

    def __str__(self):
        return f''' customer : {self.customer_name}\n account number: {self.acct_num}\n 
        date of opening: {self.date}\nBalance : ${self.balance:.02f}'''
    #make a deposit
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} has been deposited in your account')




ac_no_1 = BankAccount("Toninho Takeo", 2345, "05-05-24", 1000 )
print(ac_no_1)

