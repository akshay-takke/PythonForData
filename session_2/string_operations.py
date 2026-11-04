"""
String Operations
"""
# String Concatination

# fName = input("First Name: ")
# lName = input("Last Name: ")
# print("Your name is " +  fName + " " + lName)


name = "Akshay Takke"
print(len(name))

"""
Indexing:
    - helps to get perticular character
    - index starts from zero

Slicing:
    - helps to get a slice of a string
"""

# Indexing
order_status = "complete order"

# get third character
print(order_status[3])

# get last character
print(order_status[-1])

# Get second last character
print(order_status[-2])

# String is Immutable, We cannot make modifications to the String
# order_status[8] = "_" throws : TypeError: 'str' object does not support item assignment

print(order_status)

# Slicing 

# 0 is included and 8 is excluded
print(order_status[0:8])

# Find length of String
length = len(order_status)
print(order_status[9:length])

# Start from 9 until end of the String
print(order_status[9:])

# Start from begining but 8 is not included so until index 7
print(order_status[0:8])

# Start from 0 to end of the String
# It is as good as printing order_status
print(order_status[:])

# Print the last 5 characters
print(order_status[-5:])

# Print everything after the Space
index = order_status.find(" ")
print(order_status[index + 1:])

# Print the first word before the space
print(order_status[0:index])

# Step every second character by default it is 1
print(order_status[1:9:2])

# Reverse a String
print(order_status[::-1])

# If multiple occurance it will provide index of First Occurence
print(order_status.find("e"))

# If Character is not present it will return -1 as index
print(order_status.find("s"))

# If we use Index function and if the character is not present then it will throw Exception
# print(order_status.index("s")) # ValueError: substring not found

# Ends With returns either True or False
print(order_status.endswith("order"))

# It capitalizes the First Word of a String
print(order_status.capitalize())

order_status = "   complete order   "
# Remove Spaces Starting and Ending Spaces
print(order_status.strip())

# if we just want to remove left side spaces
print(order_status.lstrip())

# If we want to remove Right side Spaces only
print(order_status.rstrip())

order_status = "complete order"
print(order_status.replace("complete", "completed"))

orders_df = "1, 2013-07-25 00:00:00.0, 11599, CLOSED"

orders_new_df = orders_df.split(",")
print(orders_new_df)