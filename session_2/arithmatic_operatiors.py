"""
Arithmatic Operators
    +, -, *, /, //, **, %

Precidence is Left -> To -> Right
"""
bigdata_fee = 800
azure_fee = 600
bigdata_enrollments = 20
azure_enrollments = 40

total_revenue = (bigdata_fee * bigdata_enrollments 
+ azure_fee * azure_enrollments)

print(f"Total Revenue is {total_revenue} ")

avg_order_price = (bigdata_fee * bigdata_enrollments 
+ azure_fee * azure_enrollments) / (bigdata_enrollments + azure_enrollments)

print(f"Average order price is {avg_order_price}")

"""
 Mathematical Calculations works as per BODMAS rule
 B - Brackets
 O - Order
 D - Division
 M - Multiplication
 A - Addition
 S - Substraction
"""
print(5 + 8 * 8) # 69 First Mul 8 * 8 -> Add 64 + 5
print((5 + 8) * 8) # 104 First Bracket Add 5 + 8 -> Mul 13 * 8
print(15 / 4) # 3.75 Floating Value
print(15 // 4) # 3 It will return only Integer part
print(15 % 4) # 3 Gives Remainder
print(2 ** 3) # 8 It returns Power

"""
 Right Side Binding
 First 2 to the Pow 3 will be calculated
 Second 2 to the Pow of Above Ans will be calculated
 Only for in case of calculating Power
"""
print(2 ** 2 ** 3) #256

# Short hand or Compound Operators
bigdata_fee += 50
print(bigdata_fee)

# Math Library
import math

# Round it to Higher value
total_sales = - 20000.60
print(math.ceil(total_sales))

# Round it to Lower value
print(math.floor(total_sales))

# If Negative numbers and want positive
print(math.fabs(total_sales))