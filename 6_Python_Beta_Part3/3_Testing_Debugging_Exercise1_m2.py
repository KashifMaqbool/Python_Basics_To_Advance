"""
  EXERCISE - 1
• Create code for a calculator that preforms the following operations.
    • add, subtract, multiply, divide, power, exponent.
• Write unit tests for each of the method of operations. 
• Add debug traces for each method and log results.
"""


# Applying Debugging on Calculator  Program(Run Seperately)
# -----------------------------------------
import unittest
import pdb
import math


def sum_func(a,b):
    sum_result = a+b
    return sum_result
    
def subtract_func(c,d):
    subtract_result = c-d
    return subtract_result
    
def multiply_func(e,f):
    multiply_result =e*f
    return multiply_result
    
def division_func(g,h):
    try:
        division_result = g/h
        return division_result
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    
def power_func(num, power):
    power_result = math.pow(num, power)
    return power_result
    
def exponent_func(number):
    exponent_result = math.exp(number)
    return exponent_result
    

def main_function():
    pdb.set_trace() # Breakpoint for the debugging
    print("This is addition of two numbers: ", sum_func(2, 3))
    print("This is subtraction of two numbers: ", subtract_func(5, 3))
    print("This is multiplication of two numbers: ", multiply_func(5, 3))
    print("This is division of two numbers: ", division_func(10, 2))
    print("This is power of given number: ", power_func(2, 5))
    print("This is exponent of given number: ", exponent_func(5))  

if __name__ == '__main__':
    main_function()
        



# Test case: Applying Unit Testing on Calculator Program Methods(Run Seperately)
# --------------------------------
class TestCaseMethods(unittest.TestCase):
    
    # Sum tests
    def test_sum_func(self):
        self.assertEqual(sum_func(2, 3), 5)
        self.assertEqual(sum_func(-1, 1), 0)
        self.assertEqual(sum_func(0, 0), 0)
        self.assertEqual(sum_func(10, -5), 5)
    # Subtract tests
    def test_subtract_func(self):
        self.assertEqual(subtract_func(5,3), 2)
        self.assertEqual(subtract_func(0,3), -3)
        self.assertEqual(subtract_func(-5,3), -8)
        self.assertEqual(subtract_func(5,0), 5)
        
    # Multiplication tests
    def test_multiply_func(self):
        self.assertEqual(multiply_func(5, 3), 15)
        self.assertEqual(multiply_func(-2, 4), -8)
        self.assertEqual(multiply_func(0, 10), 0)

    # Division tests
    def test_division_func(self):
        self.assertEqual(division_func(10, 2), 5)
        self.assertEqual(division_func(5, 2), 2.5)
        self.assertIsNone(division_func(5, 0), None)  # Division by zero

    # Power tests
    def test_power_func(self):
        self.assertEqual(power_func(2, 3), 8)
        self.assertEqual(power_func(5, 0), 1)
        self.assertEqual(power_func(3, 2), 9)

    # Exponent tests
    def test_exponent_func(self):
        self.assertAlmostEqual(exponent_func(1), math.e)
        self.assertAlmostEqual(exponent_func(0), 1)
        self.assertAlmostEqual(exponent_func(2), math.exp(2))
        
        
if __name__ == '__main__':
    unittest.main()
        
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    