# countE.py
# This program reads in a text file and outputs the number of e's it contains.
# Author: Stefania Verduga


# We should import the sys module, which provides access to some variables
# and functions that interact with the Python interpreter.
import sys

# The variable argv allows us to access command-line arguments.
filename = sys.argv[1]

# This block of code allows us to open the specified file by 'filename'
# in read-only mode.
with open(filename, 'r') as file:
    content = file.read()

# We use the variable count to keep track of the number of 'e' characters found in the file.
# And increment count variable by one for each 'e' or 'E' found in the file.
count = 0
for char in content:
    if char == 'e' or char == 'E':
        count += 1

print(count)
