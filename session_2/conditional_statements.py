"""
Conditional Statements

"""
# Type Cast as input returns String
marks = int(input("Enter your marks: "))
"""
    Indentation is very imp
    Python dont ask for curley bases
    It enforses you write in proper block
    If not then it will throw Error
"""

"""
Comparison Operators
    == != < >  >= <=
"""
if marks > 80:
    print("A Grade")
elif marks >= 35:
    print("You pass but didn't secure A Grade")
else:
    print("Fail")
    print("Never lose hopes", "Try again")


age = int(input("Enter your age: "))
criminalRecord = input("Do you have criminal record? (Yes/No): ")

if not age < 18 and criminalRecord.lower() == "no" :
    print("Eligible for vote")
else:
    print("Not eligible for vote")

