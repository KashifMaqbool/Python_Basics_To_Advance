# Importing pdb library for the debugging purpose
import pdb

def sum_values(a,b):
    return a+b



def debug_function():
    
    pdb.set_trace() # Breakpoint
    
    """ The debugger stops the execution right after the above line and waits until
    user input is provided. When debugger stops you have to press n to run next line.
    """ 
    
    print("This is the first line.")
    print("This is the second line")
    result = sum_values(5, 10)
    print("The code is done.")
    return result

debug_function()


"""
• The first line of our test_method, has the trace. The debugger stops right 
  after executing that line. You can use controls such as n to move to the next 
  line, s to step into the function being called (as we do to access the 
  sum_values() method).
• While inside the debugger, you can access the internal variables as they are 
  created. For instance, while inside the sum_values method, you can access the 
  values of a and b.
"""