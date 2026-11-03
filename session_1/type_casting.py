""" 
Automatic Type Casting Happens
Int to Float
800.0 + 50.5 = 850.5
"""
course_fee = 800

print(course_fee + 50.5)

"""
We can only concatinate String using + operator
We cannot add Integer to String
We will not get compiletime error like java
We will get Runtime Error
"""
# print(instructor_name + 1)

print(course_fee)

# Increase Course Fees by 10%
course_fee = course_fee + (course_fee * 0.10)
print(course_fee)


# Type Casting 
"""
In big Data world 
You might read data from text file
"""

fees = "800"
print(type(fees))

# TypeError: can't multiply sequence by non-int of type 'float'
fees = int (fees) + (int (fees) * .1)
print(fees)

"""
String concate and formatting

"""

first_name = "Sumit"
last_name = "Mittal"

print(first_name + " " + last_name)

print("------" * 9)
print(f"My first name is {first_name} and my last name is {last_name}")
print("------" * 9)

# This will take input as String
salary = input("What is your current salary: ")
hike = input("What is the hike percentage: ")

# We have to Type Cast it
new_salary = int (salary) + ( int(salary) * int(hike) / 100)

print(f" The new salary after the hike is : {new_salary}")