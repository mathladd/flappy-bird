"""
Class: ETEST beginner programming class
Python Basic
Author:
Date: 

"""

from colorama import Fore

def add(x, y):
    sum = x + y
    return sum


def subtract(x, y):
    return x - y

def pow(x, y):
    return x ** y

def multiply(x, y): 
    return x * y

def multiply_add(x, y):
    z = x
    i = 1
    while i < y:
        i = i + 1
        x += z
    return x

def division_subtract(x, y):
    return
    
def pow_multiply(x, y): 
    pow = x
    i = 1
    while i < y:
        i = i + 1
        pow *= x
    return pow
    
def pop_buzz(x):
    i = 1
    while i < x:
        i += 1
        if i % 10 == 0:
            print('buzz')
        elif i % 5 == 0:
            print('pop')
    return

if __name__ == '__main__':
    print(add(1, 3), subtract(3, 1), pow(2, 3), multiply(5, 10), multiply_add(5, 10), pow_multiply(2, 3))
    pop_buzz(22)
    
    
