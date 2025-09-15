#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 14:17:39 2025

@author: kashifmaqbool
"""

# Example 1:
#-----------
""" 
Let's define a lambda function that raises any provided number by the power n.
We will then define functions using this lambda function like taking_cube, taking_square, etc.
"""
def my_power_raiser(n):
    return lambda a: a ** n


taking_square = my_power_raiser(2)  # taking_square = lambda a: a**2
taking_cube = my_power_raiser(3)
taking_quad = my_power_raiser(4)


input_number = 3
print("Our input is:", input_number)
print("taking_square function raises input by power 2:", taking_square(input_number))
print("taking_cube function raises input by power 3:", taking_cube(input_number))
print("taking_quad function raises input by power 4:", taking_quad(input_number))





# Example 2:
#-----------
"""
Lambda function use case with condition checking (nested if-else)
"""

number = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print("This number is:", number(5))
print("This number is:", number(-5))
print("This number is:", number(0))








