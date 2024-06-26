''' Variables and Operators '''
# Create a variable for your first name and a variable for your last name. Concatenate and print them in a new variable called 'fullname'.
# first_name = "John"
# last_name = "Doe"

# fullname = first_name + " " + last_name

# print("Full Name:", fullname)

# Create a variable called greeting and assign it to string value of 'hip hop hooray'. Using multiplication, create a third variable called 'three cheers' which repeats greeting 3 times.
# greeting = "hip hop hooray"

# three_cheers = greeting * 3
# print("Three cheers:", three_cheers)

''' Arithmetic Operators  '''

# add 100 to 50

# print(100 + 50)


# add 25 to 60

# print(25+60)

# multiply 5 and 5

# print(5*5)

# multiply 6 and 3

print(6*3)

# subtract 15 from 45

# subtract 60 from 100

# raise 5 to the 2nd power

# raise 6 to the 3rd power

# raise 4 to the 8th power

# 10 divided by 5

# 7 divided by 3

# 10 divided by 3, drop the remainder

# 9 divided by 5, drop the remainder

# Remainder of 14 divided by 5

# Remainder of 12 divided by 8

''' Comparison Operators '''

# Is 5 greater than 7?
# print(5>7)

# Is 10 less than 4?

# Is 8 less than or equal to 14?

# Is 10 less than or equal to 10?

# Is 6 equal to 7?

# is 100 equal to 100?

# Is 15 not equal to 11?
# print(15 != 10)



''' Strings '''

# Check if the following string is lowercase, use meaningful variable names

# day = 'tuesday'

# Check if all the characters in the text are in upper case:
# The isupper() method returns True if all the characters are in upper case, otherwise False.

# word = 'WEDNESDAY'
# check_upper = word.isupport()
# print(check_upper)

''' The isidentifier() method returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.'''

# Use the isidentifier method on the following username variables

username = '#$(@#@#$#@)'

username2 = 'simonsays_90'

username3 = '3492_sdfsdf'

username4 = 'hello*world'


# convert to lowercase

# make_me_lower_case = 'HALLOWEEN'
# make_me_lower_case = make_me_lower_case.lower()
# print(make_me_lower_case)

# convert to uppercase
# make_me_upper_case = 'valentines day'
# make_me_upper_case = make_me_upper_case.capitalize()
# print(make_me_upper_case)

# Is this proper title case?
# test_string = "the eye of the tiger"
# title_check = test_string.title()
# print(title_check)

# Put all list items in a string



# Replace J with B
# test_name = "jerry"
# replaced = test_name.replace('j','b')
# print(replaced)

# split this string and place each word in a list
string = 'I would like to split up this string'

# Check if this string starts with a letter w
# str = 'zootopia'
# result = str.startswith()
# print(str)



''' Conditionals - if/else statements '''

# Check if num 1 is greater than num 2. Print the results to the user and use a formatted string

num_1 = 10
num_2 = 9
# if num_1 > num_2 :
#     print(f'{num_1}is greater than{num_2}')
# else:
#     print(f'{num_2} is greater than {num_1}')

''' Loops - For/While'''

# Write a while loop that will count from 0 to 50
# start = 0
# end = 50
# while start <= end:
#     print(start)
#     start += 1

# Write a while loop that will count down from 65 to 25
# start = 65
# end = 25
# while start >= end:
#     print(start)
#     start -= 1



# Write a while loop that will ask start at 100 and count down to 50, however, put some logic into the loop so the loop stops at 75
#  start = 100
# end = 50
# while start >= end:
#  print(start)
#  start -= 

# Write a for loop that will loop through the string below and copy/move these letters to the new empty string'''

# str_1 = 'Have a happy birthday'
# str_2 = ''
# for s in str_1:
#  str_2 +=

    
''' Loops & Conditionals'''
# write a for loop to loop through this list and tell the user if the number is even or odd
    
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# write a for loop to loop through this string and tell the user if the number is vowel or a consonant

vowels = 'aeiou'
my_string = 'abracadabra'




# In a while loop, ask the user for their favorite animal. If the word is equal to giraffe, we will tell the user congratulations and end the loop. Otherwise we will keep prompting the user.






# In a while loop, ask the user for a word in all lowercase. If the string is not all lowercase, reprompt the user until the condition is met

# HINT The isupper() method returns True if all the characters are in upper case, otherwise False.


        
# Create a while loop, We will ask the user for a string, the first character of the string must be a number, the last character must be a capital letter to pass testing. Otherwise the user must keep trying.

# test_word = '1helloH'



''' Lists '''

# Loop through the full list, and copy all the items in that list into the empty list
# full_list = ['Move', 'me', 'to', 'an', 'empty', 'list', 'with', 'append']
# empty_list = []


# Lets practice some more indexing

my_super_list = [['superman', 'wonderwoman','batman'],['spiderman','captain america','ironman'],['aquaman']]

# Create a variable and assign it to wonderwoman via indexing


# Create a variable and assign it to spiderman via indexing


# Create a variable and assign it to aquaman via indexing


# Using a for loop, create a new list that contains any students without the letter a

# For Loop
students = ['Anna', 'Dana', 'Sarah', 'Farley', 'Oleg', 'Gionni', 'Brenetta']


# List Comprehension - new_list = [x for x in original_list if condition]
students = ['Anna', 'Dana', 'Sarah', 'Farley', 'Oleg', 'Gionni', 'Brenetta']


# List Comprehension - new_list = [expression for x in original_list]
# original_list = [1, 2, 3, 4, 5, 6]

# create a new list with 1 added to each number (no append needed)


''' Ranges '''

'''
Create the following output from the following two lists

software = ['Word', 'Excel', 'Powerpoint', 'Access']
purpose = ['word processing', 'spreadsheet', 'presentation', 'database']

Word is word processing software.
Excel is spreadsheet software
Powerpoint is presentation software
Access is database software

'''

software = ['Word', 'Excel', 'Powerpoint', 'Access']
purpose = ['word processing', 'spreadsheet', 'presentation', 'database']

# with zip
# for s,p, in zip(software, purpose):
#     print()

''' Python Exercises'''

'''
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list those numbers.

# Try the split string method
'''
# result = user_input.split(",")
# print(result)

'''
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
'''
# color_list = ["Red","Green","White" ,"Black"]
# print(f'the first color is {color_list[0]} and the last color is {color_list[-1]}')


'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615

'''


'''
Write a Python program that concatenates all elements in a list into a string and returns it.

my_list = [1, 2, 3, 4, 5]
'''

'''
Write a Python program to sum the first n positive integers.
'''



'''  Write a Python program to calculate sum of digits of a number. '''