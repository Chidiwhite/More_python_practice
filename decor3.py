# Define the decorator 'decorator_with_arguments'.
def decorator_with_arguments(function):
    # Define the wrapper function 'wrapper_accepting_arguments' that will wrap the original function 'function'.
    def wrapper_accepting_arguments(arg1, arg2):
        # Print the arguments passed to the wrapper function.
        print("My arguments are: {0}, {1}".format(arg1, arg2))
        # Call the original function 'function' with the same arguments.
        function(arg1, arg2)
    # Return the wrapper function 'wrapper_accepting_arguments'.
    return wrapper_accepting_arguments

# Apply the 'decorator_with_arguments' decorator to the 'cities' function using the '@' syntax.
@decorator_with_arguments
def cities(city_one, city_two):
    # The original function 'cities' prints the two input cities.
    print("Cities I love are {0} and {1}".format(city_one, city_two))

# Call the decorated 'cities' function with arguments "Nairobi" and "Accra".
# The 'decorator_with_arguments' decorator prints the arguments before calling the original function.
print(cities("Nairobi", "Accra"))
