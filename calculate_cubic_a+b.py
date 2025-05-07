import math
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int((math.pow(a,3))+((3*b)*(math.pow(a,2)))+((3*a)*(math.pow(b,2)))+(math.pow(b,3)))
print("The cubic of (a+b) is :",c)