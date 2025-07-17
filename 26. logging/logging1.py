#using DEBUG
import logging
logging.basicConfig(filename ='test1.log',level =logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(message)s')

def add(x,y): #adding func
    return x+y

def subtract(x,y): #subtract func
    return x-y
def multiply(x,y): #multiply func
    return x*y
def division(x,y): #division func
    return x/y
    
num1 = 10
num2 = 5

add_result = add(num1,num2)
logging.debug(f"add: {num1} + {num2}: {add_result}")

sub_result = subtract(num1,num2)
logging.debug(f"subtract: {num1} - {num2}: {sub_result}")

mul_result = multiply(num1,num2)
logging.debug(f"multiply: {num1} * {num2}: {mul_result}")

div_result = division(num1,num2)
logging.debug(f"divide: {num1} / {num2}: {div_result}")
