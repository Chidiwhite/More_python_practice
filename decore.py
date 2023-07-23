# Define the decorator 'decorfunc'.
def decorfunc(funcz_to_decor):
    # Define the wrapper function 'wrapper_func' that will wrap the original function 'funcz_to_decor'.
    def wrapper_func(*args, **kwargs):
        # Call the original function 'funcz_to_decor' with the keyword arguments ('kwargs') passed to the wrapper function.
        # The returned value from the function is stored in 'func'.
        func = funcz_to_decor(**kwargs)

        # Calculate the sum of values passed in the 'kwargs' dictionary.
        sum = 0
        for k, v in kwargs.items():
            sum += v

        # Return the sum of values passed in the 'kwargs' dictionary.
        return sum

    # Return the wrapper function 'wrapper_func'.
    return wrapper_func

# Define the function 'decorated_func'.
def decorated_func(*args, **kwargs):
    # Print a message indicating there are no arguments for 'args',
    # but there are arguments for 'kwargs'.
    print(f"There's no arguments for args - {args}\nbut there are arguments for kwargs - {kwargs}")

# Apply the 'decorfunc' decorator to the 'decorated_func' function using the '@' syntax.
# The 'decorfunc' will add additional functionality around the 'decorated_func' function.
# The wrapped function will calculate and return the sum of values in the 'kwargs' dictionary.
print(decorated_func(coffee=5, tea=7))
