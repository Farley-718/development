from datetime import datetime
import datetime

'''
Classes
'''
# Class Definition and Initializer
class Point2d:

    def __init__(self, x = 0 ,y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    

    # add your object to another object of your class
    def __add__(self, other):
        return Point2d(self.x - other.x, self.y + other.y)
    
    # subtract my object from another object

    def __sub__(self, other):
        return Point2d(self.x -other.x,self.y - other.y)
    
    # test equality from another object
    def __eq__( self , other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __lt__(self,other):
        if self.x < other.x and self.y < other.y:
            return True
        return False
# Mutator method - setter
    def set_x(self, new_x):
        self.x = new_x
    
    def set_y(self, new_y):
        self.y = new_y
    # accessor methods
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    






# creating an object of the Point2d class 
point1 = Point2d(4,10)
point2 = Point2d(5,9)

# Accessor method




# Return a string representation of this object
print(point1)
print(point2)
    
# Adds this object to another object from the same class, return a new object.
    
    
# Subtracts another object from this object, return a new object.
    

# Test equality between this object and another, return a boolean.

point3 = Point2d(3,4)
point4 = Point2d(3,4)
print(point3 == point4)


#less than function
point5 = Point2d(10,12)
point6 = Point2d(13, 15)
print(point6>point5)

# Mutator method - setter
point7 = Point2d(5,11)
point7.set_x(10)# out method will change the value of x
print(point7)

point7.set_y(25)
print(point7)

# Accessor method
print(point7.get_x())

# Create a point object with attributes x=2, y=3

# Let’s add a __str__ method to our Point2D class so we can print Point2D objects.


# Lets add __add__ to add objects of the same class together


# Lets try __sub__ to add objects of the same class together

# Let's try __eq__ method to test equality
'''What is the output of this code if we don't override ==?
What is the output if we override == to use value equality?
Is it the same or different? Why?

Without the __eq__ method, we will only be able to test if it is the same object
'''



# Let's try __lt__ method to test less than


# Setting with mutator methods



# Getting with accessor methods





''' Exercise - Date Class '''




 




'''
Exercise - Dog Class
this class will take 3 parameters , dog name , dog breed , a
'''
class Dog :
    def __init__(self,name,birth_year, breed):
        self.name = name
        self.birth_year = birth_year
        self.breed = breed
    
    def __str__(self):
    
        return f'{self.name} is a {self.breed} and was born in {self.birth_year}'
    
    def human_age(self):
        today = datetime.datetime.now()
        year = today.year
        # return f'{self.name} is {year - self.birth_year} years old in human years'

    def dogyears(self):
        return 7 * self.human_age()
    


dog1 = Dog('Fido',2020 , 'Golden Retriver')# created our first object of dog class
dog2 = Dog('Zuzu',2021, 'dacsund')
dog3 = Dog('Pierre', 2013, 'Pitbull')
# print(dog1)
# print(dog2)
# print(dog3)


today = datetime.datetime.now()
year = today.year
# print(year)
# print(dog1.human_age())
# print(dog2.human_age())
# print(dog3.human_age())

'''Excercise - date class
1. display the date in a format'''

class Date:
    def __init__(self,year= 1970 , month=1 , day=1):
        ''' these are our parameters'''
        self.year = year
        self.month = month 
        self.day = day 
    def __str__(self):
        return f'Month :{self.month: 02d} \ nDay: {self.day :02d}\nYear : {self.year}'
    def __eq__(self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return False
    