''' This program calculates the perimeter of a triangle

Requirements
    - Comment your code 
        +5
    - Assign meaningful variable names 
        +5
    - Output a print statement, "The perimeter of your triangle is..." 
        +5
    - The test case for your program is side # 1 is 5, the base is 6, side # 2 is 10 
        +5
    - Output a print statement, "Is side 1 greater than side 2?" 
        +5
    - Output a print statement, "Is the base equal to side 1?"
        +5
'''
side1_length = 5
base_length = 6
side2_length = 10

# output test case values
print("test case:")
print("Side #1:",side1_length)
print("base:",base_length)
print("side #2:" , side2_length)

# calculate perimeter
perimeter =side1_length + side2_length + base_length
print("The perimeter of the triangle is:",perimeter)
# output whether side 1 greater than side 2?
print("Is side 1 greater than side 2?")
if side1_length > side2_length:
    print("yes")
else:
    print("no")
