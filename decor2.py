# Define the decorator 'splitdecor'.
def splitdecor(function):
    # Define the wrapper function 'makesplit' that will wrap the original function 'function'.
    def makesplit(text):
        # Call the original function 'function' with the input 'text' and store the result in 'func'.
        func = function(text)
        # Split the 'func' (result of the original function) into a list of words and return it.
        return func.split()
    # Return the wrapper function 'makesplit'.
    return makesplit

# Define the decorator 'makeupper'.
def makeupper(function):
    # Define the wrapper function 'doupper' that will wrap the original function 'function'.
    def doupper(text):
        # Call the original function 'function' with the input 'text' and store the result in 'func'.
        func = function(text)
        # Convert the 'func' (result of the original function) to uppercase and return it.
        return func.upper()
    # Return the wrapper function 'doupper'.
    return doupper

# Apply the 'splitdecor' decorator first, then the 'makeupper' decorator to the 'word' function using the '@' syntax.
@splitdecor
@makeupper
def word(text):
    # The original function 'word' returns the input 'text' as it is.
    return text

# Call the decorated 'word' function with input 'wicked nosense man'.
# The 'splitdecor' decorator first splits the result into words,
# then the 'makeupper' decorator converts the result to uppercase.
# The final output is a list of words in uppercase: ['WICKED', 'NOSENSE', 'MAN'].
x = word('wicked nosense man')
print(x)
