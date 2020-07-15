# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
        '''because True is not a default return, 
        False must also be coded in if you want an 
        odd number to return anything other than 'none''''

print(is_even(3), '**False expected') 
print(is_even(4), '**True expected')

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

