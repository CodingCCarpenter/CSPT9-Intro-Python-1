"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

''' same as: 
y = []
for i in range(1, 6):
    y.append(i)
'''

y = [item for item in range(1, 6)] # could also say range(6)
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

'''same as:
y = []
for i in range(1, 10):
    y.append(i**3)
'''
y = [item ** 3 for item in range(1, 10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

'''same as: 
y = []
for i in a:
    y.append(i.upper)
'''

a = ["foo", "bar", "baz"]

y = [item.upper for item in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [int(item) for item in x if int(item) % 2 == 0]

print(y)