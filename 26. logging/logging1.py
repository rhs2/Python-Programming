#using DEBUG
import logging
logger = logging.getLogger(__name__) #setting up logger for different root.
file_handler = logging.FileHandler('test1.log')
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
formatter = logging.Formatter('%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
#1. creating logger __name__
#2. creating file_handler
#3. adding file handler to logger
#4. creating formatter
#5. adding that formatter to file handler
#6. creating logger level

def add(x,y): #adding func
    return x+y

def subtract(x,y): #subtract func
    return x-y
def multiply(x,y): #multiply func
    return x*y
def division(x,y): #division func
    return x/y
    
num1 = 10
num2 = 7

add_result = add(num1,num2)
logger.debug(f"add: {num1} + {num2}: {add_result}")

sub_result = subtract(num1,num2)
logger.debug(f"subtract: {num1} - {num2}: {sub_result}")

mul_result = multiply(num1,num2)
logger.debug(f"multiply: {num1} * {num2}: {mul_result}")

div_result = division(num1,num2)
logger.debug(f"divide: {num1} / {num2}: {div_result}")
