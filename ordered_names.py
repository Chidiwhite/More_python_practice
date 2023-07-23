# Import required modules
from collections import OrderedDict
from operator import getitem

# Get the number of people as input
N = int(input())

# Get the details of each person as input and store in a list of lists 'people'
people = [input().split() for i in range(N)]

# Initialize an empty dictionary 'record' to store person details
record = {}

# Loop through each person's details and create a dictionary 'd' for each person
for i, person in enumerate(people):
    d = {}
    # Assign 'id', 'age', and 'sex' keys to the dictionary 'd' based on the input
    d['id'] = i + 1
    d['age'] = int(person[-2])
    d['sex'] = str(person[-1])
    
    # Generate the person's name based on sex ('M' for male, 'F' for female)
    if person[-1] == "M":
        name = "Mr. " + " ".join(person[:2])
    else:
        name = "Ms. " + " ".join(person[:2])
    
    # Add the person's name and details to the 'record' dictionary
    record[name] = d

# Sort the 'record' dictionary based on the 'age' key using OrderedDict
sorted_record = OrderedDict(sorted(record.items(), key=lambda x: getitem(x[1], 'age')))

# Print the sorted 'record' dictionary
print(sorted_record)

# Print the names of people in sorted order (based on age)
for name in sorted_record:
    print(name)




# # 3
# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F
# print(people)
# print(age)
# print(sorted_age)