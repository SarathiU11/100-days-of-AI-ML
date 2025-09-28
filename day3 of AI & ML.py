# variable and data type#

#strimg
name ="sarathi"

#integer
age  = 42

#float
height =5.8

#boolean
is_student= False

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

mage ="42"
myage = int(mage)
print(myage + 5)
print("hello " + name  +"!" )
print(f"hello {name} good morning ")
print("hello my friend ,{}!",format(name))

#project 2 - personalized greeting program

name = input("what is your name?")
age = int(input("how old are you"))
color =input("what is your favorite colour?")

print("n---- personalized greeting---")
print(f"hello, {name}! ")
print(f"you are {age} years are old and {color} is a beatiful color !")
print("good to have in the python ")


s