#PYTHON Calculator

import math
operator=input("Enter an operator;+,-,*,/")
n1=float(input("Enter the first number: "))
n2=float(input("Enter the second number: "))
if operator == "+":
    result= n1+n2
    print(round(result,2))
elif operator == "-":
    result = n1 - n2
    print(round(result, 2))#round(x,n) where n is the decimal place upto which we want to round off the number
elif operator == "*":
    result = n1 * n2
    print(round(result, 2))#round(x,n) where n is the decimal place upto which we want to round off the number
elif operator == "/":
    result= n1 / n2
    print(round(result, 2))#round(x,n) where n is the decimal place upto which we want to round off the number
else:
    print(f"{operator} is an invalid operator")