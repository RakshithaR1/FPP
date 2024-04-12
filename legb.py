#L-Local,E-Enclosed,G-Global,B-built-in
# Global scope
global_var = "I'm global"

def outer_function():
    # Enclosing scope
    enclosing_var = "I'm enclosing"
    
    def inner_function():
        # Local scope
        local_var = "I'm local"
        print(local_var)  # Accessing local variable
        print(enclosing_var)  # Accessing enclosing variable
        print(global_var)  # Accessing global variable
    
    inner_function()

outer_function()

# Define a decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Define a function to be decorated

def say_hello():
    print("Hello!")

# Apply the decorator
@my_decorator
def decorated_say_hello():
    print("Hello!")

# Call the original function
print("Calling original function:")
say_hello()

# Call the decorated function
print("\nCalling decorated function:")
decorated_say_hello()

def leap_year(year):
    
    match year % 4, year % 100, year % 400:
        case (0, 0, 0):
            print("The year is a leap year.") 
        case (0, 0, _):
            print("The year is not a leap year.")  # Divisible by 4 and 100, but not 400 => Not a leap year
        case (0, _, _):
            print("The year is a leap year.")  # Divisible by 4, but not by 100 => Leap year
        case (_, _, _):
            print("The year is not a leap year.")  # Not divisible by 4 => Not a leap year

y = int(input("Enter the year: "))
leap_year(y)
         