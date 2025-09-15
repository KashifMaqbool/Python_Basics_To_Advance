""" Suppose, you have a piece of code that takes argument from the user their f
irst and last name and returns each capitalized and joined as a single string.
"""

# Piece of code
def join_names(fname,lname):
    return " ".join([fname.capitalize(), lname.capitalize()])

data = join_names('kashif', 'maqbool')
print(data) 


"""
Let’s write a test case to ensure that our code does the following things it is supposed to:
• Return a data type of string
• The string contains two words that are separated by space 
• Each of those words is capitalized

Intention is to ensure our code behaves exactly how we want them to. Hence, you can work on improving your 
code as long as it returns two strings which are capitalized.
"""


# Applying Test Case 
import unittest
class TestCaseMethods(unittest.TestCase):
    
    def test_type_check(self):
        self.assertEqual(type(data), str)
        
    def test_length_check(self):
        self.assertTrue(len(data.split(" ")),2)
        
    def test_is_capitalized(self):
        temp1, temp2 = data.split(" ")
        self.assertTrue(temp1.istitle())
        self.assertTrue(temp2.istitle())
        
if __name__ == "__main__":
    unittest.main()
    
    
    


