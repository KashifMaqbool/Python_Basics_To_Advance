#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 14:30:18 2025

@author: kashifmaqbool
"""


"""
1. Recreate the calculator as a class.
    • Treat it as a parent class.
    • Create a class called ScientificCalculator and inherit Calculator
    • Create scientific functions: log, power, exponent and factorial as lambda functions.
2• Set decorator function which prints the inputs and the operation being performed. 
    . [e.g. for addition, the decorator function must print the arguments of the function as ‘1 + 3 = 4‘]
"""

# Decorator
#-----------
import math

def calculator_decorator(func):
    def internal_wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        
        # Map functions names to operator symbols to display desired output.
        operators = {
        "sum_func": "+",
        "subtract_func": "-",
        "multiply_func": "*",
        "division_func": "/",
        "power": "^",
        "exponent": "exp",
        "log": "log",
        "factorial": "!"
        }
        
        # Get the operator symbol based on the function name (e.g., "sum_func" → "+").
        # If the function name is not found in the dictionary, use "?" as a default.

        operator = operators.get(func.__name__, "?")
        
        # Printing in desired output
        if len(args) == 2:
            print(f"{args[0]} {operator} {args[1]} = {result}")
        elif len(args) == 1:
            print(f"{args[0]} {operator} = {result}")
        else:
            print(f"Result: {result}")
            
            
        return result
    return internal_wrapper


# Parent Class: Calculator
#-------------------------

class Calculator:
    
    @calculator_decorator
    def sum_func(self, a, b):
        sum_result = a+b
        return sum_result
    
    @calculator_decorator
    def subtract_func(self, c, d):
        subtract_result = c-d
        return subtract_result
    
    @calculator_decorator    
    def multiply_func(self, e, f):
        multiply_result =e*f
        return multiply_result
    
    @calculator_decorator
    def division_func(self, g, h):
        try:
            division_result = g/h
            return division_result
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            
            
# Child class: ScientificCalculator
#----------------------------------
            
class ScientificCalculator(Calculator):
    
    power_func = calculator_decorator(lambda self, a, b: math.pow(a,b))
    exponential_func = calculator_decorator(lambda self, a: math.exp(a))
    log_func       = calculator_decorator(lambda self, a: math.log(a))
    factorial_func = calculator_decorator(lambda self, a: math.factorial(a))    


# Main execution
#---------------

if __name__ == '__main__':
    sci_cal = ScientificCalculator()
    
# Calculator functions
print("Simple Calculator Output:")
sci_cal.sum_func(3, 2)
sci_cal.subtract_func(5, 1)
sci_cal.multiply_func(9, 10)
sci_cal.division_func(100, 10)

# ScientificCalculator functions
print(" ")
print("Scientific Calculator Output:")
sci_cal.power_func(2,3)
sci_cal.exponential_func(5)
sci_cal.log_func(9)
sci_cal.factorial_func(5)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    