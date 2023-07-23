# Define the decorator 'hello_decorator'.
def hello_decorator(func):
    # Define the wrapper function 'inner1' that will wrap the original function 'func'.
    def inner1(*args, **kwargs):
        # Print a message before the execution of the original function.
        print("before Execution")

        # Call the original function 'func' with the input arguments ('args' and 'kwargs').
        # The returned value from the function is stored in 'returned_value'.
        returned_value = func(*args, **kwargs)

        # Print a message after the execution of the original function.
        print("after Execution")

        # Return the value returned by the original function to the caller.
        return returned_value

    # Return the wrapper function 'inner1'.
    return inner1

# Define the function 'sum_two_numbers'.
def sum_two_numbers(a, b):
    # Print a message inside the function.
    print("Inside the function")
    # Return the sum of 'a' and 'b'.
    return a + b

a, b = 1, 2

# Apply the 'hello_decorator' decorator to the 'sum_two_numbers' function using the '@' syntax.
# The 'hello_decorator' will add additional functionality around the 'sum_two_numbers' function.
# The wrapped function will print messages before and after the original function execution.
# The return value of the 'sum_two_numbers' function will be printed outside the decorator.
print("Sum =", sum_two_numbers(a, b))
