# 1. Function Decorators
#-----------------------

# Example 1
def function_decorator(func):
    def wrapper():
        print("Starting Function.")
        func()
        print("Ending Function.")
    return wrapper
    
@function_decorator   
def greet():
    print("Assalam-o-Alaikum!")
    
greet()



# Example 2
def extract_function_name(func):
    def internal_wrapper_function(*args, **kwargs):
        print("Starting of the Function.")
        returned_value = func(*args, **kwargs)
        print("Ending of the Function.")
        return returned_value
    return internal_wrapper_function


@extract_function_name
def sum_function(a,b):
    print("This is calling sum_function().")
    return a+b

@extract_function_name
def multiply_function(a,b):
    print("This is calling multiply_function().")
    return a*b


def main_function():
    a,b = 2,3
    print("The sum of values from sum_function() is: ", sum_function(a, b))
    print("The multiply of values from multiply_function is: ", multiply_function(a, b)) 
    
main_function()






# Methods Decorators
#-------------------
def method_decorators(func):
    def internal_wrapper_method(self, *args, **kwargs):
        print("Starting of the Function.")
        returned_value = func(self, *args, **kwargs)
        print("Ending of the Function.")
        return returned_value
    return internal_wrapper_method

class MyClass:
    @method_decorators
    def greet(self):
        print("Assalam-o-Alaikum!")
        
obj = MyClass()
obj.greet()






# 3. Class Decorators
#-----------------
def decorator(cls):
    cls.greet_attribute = "Assalam-o-Alaikum!"
    return cls

@decorator
class MyClass:
    pass

obj = MyClass()
print(obj.greet_attribute)






# 4. Built-in Decorators (Python-provided)
#-------------------------------------
class Example:
    @staticmethod
    def static_method():
        return "Static method"

    @classmethod
    def class_method(cls):
        return "Class method"

    @property
    def my_property(self):
        return "Property value"





# Nested Decorators (Stacked Decorators)
#-------------------------------------
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def greet():
    print("Assalam-o-Alaikum!")

greet()








































