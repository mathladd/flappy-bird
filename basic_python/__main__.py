"""
Class: ETEST beginner programming class
Python Basic
Author:
Date: 

"""

from colorama import Fore

def add(x, y):
    """This function adds 2 numbers"""
    sum = x + y
    return sum


def subtract(x, y):
    """This function subtracts y from x"""
    return

def pow(x, y):
    """This function returns x to the power of y"""
    return

def multiply(x, y): 
    """This function multiplies x with y through 
    built-in Python multiplication implementation"""
    return

def multiply_add(x, y):
    """This function multiplies x with y by addition(s)
    instead"""
    return

def division_subtract(x, y):
    """This function divides x by y through 
    subtraction(s)"""
    return
    
def pow_multiply(x, y): 
    """This function returns x to the power of y, 
    through multiplication"""
    return
    
def pop_buzz(x):
    """This function accepts an input x value, and 
    from 1 to x, if it encounters a number divisible 
    by 5, it will print a "Pop". Moreover, if it encounters
    a number divisible by 10, a "Buzz" will also be printed out"""
    return

if __name__ == '__main__':
    print(Fore.GREEN)
    print('add', str(add(1, 3)) + Fore.BLUE) 
    print('subtract', str(subtract(3, 1)) + Fore.YELLOW)
    print('pow', str(pow(2, 3)) + Fore.MAGENTA)
    print('multiply', str(multiply(5, 10)) + Fore.RED)
    print('multiply_add', str(multiply_add(5, 10)))
    print('pow_multiply', str(pow_multiply(2, 3)))
    pop_buzz(22)
    
    
