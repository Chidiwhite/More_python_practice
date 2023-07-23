# Define the decorator function 'decorfunc'.
def decorfunc(func):
    # Define the wrapper function that will wrap the original function 'func'.
    def wrapper(*args, **kwargs):
        # Print the input arguments ('args' and 'kwargs') of the wrapped function.
        print(f'for args = {args}, for kwargs = {kwargs}')
        # Call the original function 'func' with the input arguments and store the result.
        function = func(*args)
        # Return the result of the original function.
        return function
    # Return the wrapper function.
    return wrapper

# Apply the decorator 'decorfunc' to the 'arguments' function using the '@' syntax.
@decorfunc
def arguments(*args, **kwargs):
    # The wrapped function 'arguments' prints its input arguments ('args' and 'kwargs').
    print(f"arguments or args = {args} \nand arguments for kwargs = {kwargs}\n")

# Call the decorated 'arguments' function with arguments (1, 2, 3, 4).
# The decorator 'decorfunc' will print the input arguments, and then
# the 'arguments' function will print its own input arguments.
print(arguments(1, 2, 3, 4))
