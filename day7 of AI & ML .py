def function_name():
    print("hello world !")
    print("this the world")
function_name()

def function(name):
    print(f"hi , i am {name}")
function("sarathi")


def add(a,b):
    print(f"the sum is : {a+b}")

add(5,4) 

def multiply(a,b):
  return a*b

result = multiply(5,4)
print("the result is:",result)

# project - basic maths quizz game #
import random

def generate_question():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operatoe = random.choice(['+','-','*']) 