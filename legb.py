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
