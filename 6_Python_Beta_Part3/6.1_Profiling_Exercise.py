#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 18:07:14 2025

@author: kashifmaqbool
"""

"""
Exercise
1. Create both calculators in exercise 2 (Calculator and Scientific Calculator).
2. Write two methods, each creates object of each of the above class and runs all the corresponding methods.
    • Which runs faster and why?
    • Which aspect of each calculator takes the longest? 
    • Which operation is performed the fastest?
"""





# Simple Calculator
#------------------

import cProfile

class Calculator:
    
    def sum_func(self, a, b):
        sum_result = a+b
        return sum_result
    
    def subtract_func(self, c, d):
        subtract_result = c-d
        return subtract_result
    
    def multiply_func(self, e, f):
        multiply_result =e*f
        return multiply_result
    
    def division_func(self, g, h):
        try:
            division_result = g/h
            return division_result
        except ZeroDivisionError:
            print("Cannot divide by zero!")


def main_function_calculator():
    
    cal = Calculator()
    
    print("Simple Calculator Output:")
    cal.sum_func(3, 2)
    cal.subtract_func(5, 1)
    cal.multiply_func(9, 10)
    cal.division_func(100, 10)
    
if __name__ == "__main__":
    cProfile.run('main_function_calculator()')
            
            
            

            
# Scientific Calculator
#----------------------    
import math
import cProfile   
            
class ScientificCalculator(Calculator):
    
    def power_func(self, a, b):
        return math.pow(a, b)

    def exponential_func(self, a):
        return math.exp(a)

    def log_func(self, a):
        return math.log(a)

    def factorial_func(self, a):
        return math.factorial(a)


def main_function_scientific_calculator():
    
    sci_cal = ScientificCalculator()
    
    print(" ")
    print("Scientific Calculator Output:")
    sci_cal.power_func(2,3)
    sci_cal.exponential_func(5)
    sci_cal.log_func(9)
    sci_cal.factorial_func(5)

if __name__ == "__main__":
    cProfile.run('main_function_scientific_calculator()')








