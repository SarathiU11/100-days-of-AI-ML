# if-else #

#if condition:
#print statement
# #else:
#print statement#

number = 10

if number > 5:
    print("the  number is greater than 5.")
elif number == 5:
    print("the number is equal to 5")
else:
    print("the number is less than 5") 
    
    
a = 7
b = 16

if a > 5 or b < 15 :
    print("both condition are true")
else:
    print("at least one condition is false ")
    
    
# day 4 projecct : number comparision tool

num1 =int(input("enter the first number: "))
num2 =int(input("Enter the second number: "))

print("\n---comparsion result ----")

if num1 == num2:
    print(f"Both number are equal: {num1}")
elif num1 > num2:
    print(f"{num1} is greater  than {num2}")
else:
    print(f"{num2} is greater than {num1}")
    
    
if num1 == 0 or num2 == 0:
    print("one number is zero")
else:
    print("the number is non -zero")