''' Tuples & Sets '''

'''
Fun Facts about Tuples
    -ordered and unchangeable (example, storing a username and password, storing an RGB value that must not change)
    -can't add or remove items
    -round brackets
    -faster than lists
    -used to store constants
    -used heterogeneous data structures (integers, floats, strings, etc) for example someone's age, gender and last name, (15, 'M', 'JONES')
    -heterogenous data structures save memory. why? lists need to over-allocate to account for new elements
    -readability
    -lets the programmer or other programmer know, this data collection should not be altered
'''
# Count & Indexing

my_number_tuple = (1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8, 8, 8, 9, 10, 10, 10, 10)

# Use the count Tuple method to count how many instances we have for 2, 3, 8, 9, 10



my_letter_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
# Use the index tuple method to return the position of letters b, d, f, h, and i

# print(my_letter_tuple.index('b'))
# print(my_letter_tuple.index('d'))
# print(my_letter_tuple.index('f'))
# print(my_letter_tuple.index('g'))
# print(my_letter_tuple.index('h'))
# print(my_letter_tuple.index('i'))
# Unpacking
user = ('Joe', 'Smith', 24)
fname ,lname, age = user
# print(fname)
# print(lname)
# print(age)
# Loop through list of Tuples

# weekdays = [("Monday", 1), ("Tuesday", 2), ("Wednesday", 3), ("Thursday", 4), ("Friday", 5), ("Saturday", 6), ("Sunday", 7)]
# for day , num in weekdays:
#     print(f'{day}is day {num}of the week')

# Adding tuples
# first_tuple = (1, 2, 3)
# second_tuple = (4, 5, 6)

# third_tuple = first_tuple + second_tuple
# print(third_tuple)

'''You have a tuple of months:
months = ("January","February","March","April","May","June", "July","August","September","October","November","December")
Use these tuples to make a list of tuples where each tuple contains a number and the month it corresponds to, like this: [("January",1),...,("December",12)]
Now print each month and its number using tuple unpacking in a for loop. The first line of output should look like this:
January is month 1 of the year.
'''
months = ("January","February","March","April","May","June", "July","August","September","October","November","December")
numbers = (1,2,3,4,5,6,7,8,9,10,11,12)


# Create List of Tuples
calender = [] # this will hold our list of tuples 
for n in range(len(months)):
    calender.append((months[n],numbers[n]))
# print(calender)

# Use a for loop to unpack and generate strings
# for m , n in calender:
#     print(f'{m} is month {n} of the year')



'''
Fun Facts about Sets
-unordered, unchangeable*, and unindexed.
* The items are unchangeable, but you can add and remove items.
Sets do not allow duplicates, so they are used to store a set of unique values. You use curly brackets for sets: { }
Because sets are unordered, you can't index them like a list. They don't have indexes at all. You can still loop through a set with a for loop.'''


# Ways to create a set
i_am_empty = set()

# What am I?


# Pass in a list
my_fav_colors_list = ['green', 'blue', 'red']
# my_fav_colors_list = set(my_fav_colors_list)
# print(my_fav_colors_list)
# print(type(my_fav_colors_list))

# Unordered
my_unordered_set = {'blue', 'green', 'red', 'orange'}
# print(my_unordered_set)


# Unchangeable
my_unchangeable_set = {'hello', 'welcome', 'to', 'newyork'}
# my_unchangeable_set[3]= 'vermont'
# print(my_unchangeable_set)
# Unindexed
my_unindexable_set = {'I', 'cant', 'be', 'indexed'}

# Break up a string



# No duplicates allowed
# my_cars = {'chevy', 'toyota', 'ford', 'ford', 'honda', 'honda'}

# No duplicates - How did we solve this problem before?

'''
8. Exercise: Removing All Duplicates
You have a list storing important data for your company, but it contains some duplicate entries. 
Go through your list and remove all the duplicates. When you're done, each item should appear in 
the list exactly once.
'''
''' With a for loop and appending'''

#original list
# states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']




''' With sets and returning a list '''

# states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']
# new_states = list(set(states))
# print(new_states)
# We can loop through sets


# top_ten_movies = {'shawshank redemption', 'avatar', 'avengers', 'its a wonderful life'}


# Let's add silver .add()
colors = {'blue', 'green', 'red'}
colors.add('silver')
# print(colors)

# Lets clear all our items .clear()
# transportation = {'cars', 'bikes', 'plane'}


# Lets create a copy .copy()
sitcoms = {'friends', 'seinfeld', 'honeymooners'}
# comedy = sitcoms.copy()
# print(id(sitcoms))
# print(id(comedy))

# Remove vermont from our set
states = {'california', 'new york', 'vermont', 'connecticut'}
states.remove('vermont')
print(states)

# Difference - What's different?
student_set = {'oleg', 'anna', 'farley'}
student_set_2 = {'oleg', 'anna', 'brenetta'}


# Intersect - What do we have in common?
my_schedule = {'mon', 'wed', 'thurs'}
dana_schedule = {'wed', 'fri', 'sat'}


# Union - uniquely list every pet
sarah_pets = {'dog', 'cat', 'bird'}
isaiah_pets = {'chickens', 'dog', 'fish'}
khadaziah_pets = {'bird', 'dog', 'fish'}
brenetta_pets = {'turtle'}
# result = sarah_pets.union(| isaiah_pets | khadaziah_pets | brenetta_pets)
# print(result)



# Symmetric difference - Items outside of matching items

# my_books = {'catcher in the rye', 'richest man in babylon'}
# her_books = {'catcher in the rye', 'richest man in babylon', 'sounder'}
# result = my_books ^ her_books

'''
Exercise - Sets
You work for a sales company and must generate a set of all customers who get a certain discount. The criteria for getting a discount is that they're over 60 years old and have made at least 5 purchases.
You have a set of customers over 60, and a set of customers who have made at least 5 purchases. Use a set operation to output a set of customers that fit both criteria for the discount. You can do this in one line of code.
Example:
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}
Output: {'Dominic', 'Simone'}
'''

# Solve with an intersection - solve with 1 or 2 lines of code
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}



print('''
Exercise - Sets
See flowchart
You work at a company where some people know Python, some people know JavaScript, and some people know both.
In a loop, prompt the user to input an employee name, whether they know Python, and whether they know JavaScript. Use this to build two sets: a set of employees that know Python, and a set of employees that know JavaScript.
Use set operators to compute the following sets:
The set of employees that know both Python and JavaScript
The set of employees that know JavaScript, but not Python
The set of employees that know Python or JavaScript, but not both ''')

# user instructions
print(''' Python and js devloper tracker instructions 
      input 's' or 'stop' at anytime''')


# initialize our variables

# put our error messages in a tuple 

# While loop

# User inputs
dev_type_iput , dev_name_input = '', ''
# string methods

# break keyword, continue, if statement

# print statement, formatted strings

# sets




