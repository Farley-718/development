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
side_1 = 5
base = 6
side_2 = 10

# calculate the perimeter of the triagle
perimeter = side_1 + base + side_2

# Output the perimeter of the triangle
print("The perimeter of your triangle is :", perimeter)

# checking to see if side_1 is greater than side_2
if side_1 > side_2 :
    print("Is side 1 graeter than side 2 ? Yes")
else: print("Is side 1 greater than side 2 ? No")

# checking if the base is equal to side_1 
if base == side_1:
    print("Is the base equal to side 1 ? Yes ")
else:
    print("Is the base equal to side 1 ? No ")
