# More_python_practice
Code 1: Decorator Function for Printing Arguments
This code defines a decorator function 'decorfunc' that wraps another function 'arguments'. The decorator prints the input arguments ('args' and 'kwargs') of the wrapped function before calling it. The 'arguments' function also prints its input arguments. When calling 'arguments(1, 2, 3, 4)', the decorator prints the input arguments, and then 'arguments' prints its own input arguments.

Code 2: Chained Decorators for Text Processing
This code defines two decorators 'splitdecor' and 'makeupper' that wrap the 'word' function. 'splitdecor' splits the input text into a list of words, while 'makeupper' converts the result of 'splitdecor' to uppercase. When calling 'word('wicked nosense man')', the output is ['WICKED', 'NOSENSE', 'MAN'].

Code 3: Decorator with Arguments
This code defines a decorator 'decorator_with_arguments' that wraps the 'cities' function. The decorator prints the arguments passed to the wrapped function before calling it. The 'cities' function prints the cities it loves. When calling 'cities("Nairobi", "Accra")', the decorator prints the arguments, and then 'cities' prints its own output.

Code 4: Decorator with Pre and Post Execution Messages
This code defines a decorator 'hello_decorator' that wraps the 'sum_two_numbers' function. The decorator prints a message before and after the execution of the original function. When calling 'sum_two_numbers(1, 2)', the decorator prints the messages, and 'sum_two_numbers' prints the sum of the two numbers.

Code 5: Decorator to Calculate the Sum of Keyword Arguments
This code defines a decorator 'decorfunc' that wraps the 'decorated_func' function. The decorator calculates and returns the sum of values passed in the 'kwargs' dictionary. When calling 'decorated_func(coffee=5, tea=7)', the decorator calculates the sum (12) and prints it.

Code 6: Sorting and Organizing Records
This code takes input for the number of people and their details. It creates dictionaries for each person and sorts them based on age using OrderedDict. The output is a sorted dictionary of people's details based on age, followed by the names of people in sorted order.
