"""
  EXERCISE - 1
• Create code for a calculator that preforms the following operations.
    • add, subtract, multiply, divide, power, exponent.
• Write unit tests for each of the method of operations. 
• Add debug traces for each method and log results.
"""


# Applying Debug logging on Calculator  Program
# -----------------------------------------
import unittest
#import pdb
import logging
import math


# Configure logging to display debug messages
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    Each method includes debug logging to trace its execution and results.
    """

    def sum_func(self, a, b):
        logging.debug(f"Adding: {a} + {b}")
        sum_result = a+b
        logging.debug(f"Addition_result: {sum_result}")
        return sum_result
        
    def subtract_func(self, c, d):
        logging.debug(f"Subtracting: {c} - {d}")
        subtract_result = c-d
        logging.debug(f"Subtract_result: {subtract_result}")
        return subtract_result
        
    def multiply_func(self, e, f):
        logging.debug(f"Multiplying: {e} - {f}")
        multiply_result =e*f
        logging.debug(f"Multiplying_result: {multiply_result}")
        return multiply_result
        
    def division_func(self, g, h):
        try:
            logging.debug(f"Divisioning: {g} - {h}")
            division_result = g/h
            logging.debug(f"Divisioning_result: {division_result}")
            return division_result
        except ZeroDivisionError:
            logging.debug("Cannot divide by zero!")
        
    def power_func(self, num, power):
        logging.debug(f"Taking power: {num} - {power}")
        power_result = math.pow(num, power)
        logging.debug(f"Powering_result: {power_result}")
        return power_result
        
    def exponent_func(self, number):
        logging.debug(f"Exponent of: {number}")
        exponent_result = math.exp(number)
        logging.debug(f"Exponent result: {exponent_result}")
        return exponent_result
    


        

# Test case: Applying Unit Testing on Calculator Program Methods
# --------------------------------
class TestCaseMethods(unittest.TestCase):
    """Set up a new Calculator instance before each test."""
    cal = Calculator()
    
    # Sum tests
    def test_sum_func(self):
        self.assertEqual(self.cal.sum_func(2, 3), 5)
        self.assertEqual(self.cal.sum_func(-1, 1), 0)
        self.assertEqual(self.cal.sum_func(0, 0), 0)
        self.assertEqual(self.cal.sum_func(10, -5), 5)
    # Subtract tests
    def test_subtract_func(self):
        self.assertEqual(self.cal.subtract_func(5,3), 2)
        self.assertEqual(self.cal.subtract_func(0,3), -3)
        self.assertEqual(self.cal.subtract_func(-5,3), -8)
        self.assertEqual(self.cal.subtract_func(5,0), 5)
        
    # Multiplication tests
    def test_multiply_func(self):
        self.assertEqual(self.cal.multiply_func(5, 3), 15)
        self.assertEqual(self.cal.multiply_func(-2, 4), -8)
        self.assertEqual(self.cal.multiply_func(0, 10), 0)

    # Division tests
    def test_division_func(self):
        self.assertEqual(self.cal.division_func(10, 2), 5)
        self.assertEqual(self.cal.division_func(5, 2), 2.5)
        self.assertIsNone(self.cal.division_func(5, 0))  # Division by zero

    # Power tests
    def test_power_func(self):
        self.assertEqual(self.cal.power_func(2, 3), 8)
        self.assertEqual(self.cal.power_func(5, 0), 1)
        self.assertEqual(self.cal.power_func(3, 2), 9)

    # Exponent tests
    def test_exponent_func(self):
        self.assertAlmostEqual(self.cal.exponent_func(1), math.e)
        self.assertAlmostEqual(self.cal.exponent_func(0), 1)
        self.assertAlmostEqual(self.cal.exponent_func(2), math.exp(2))
        
        
if __name__ == '__main__':
    logging.info("Running all Unit Tests.")
    unittest.main()
        
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    