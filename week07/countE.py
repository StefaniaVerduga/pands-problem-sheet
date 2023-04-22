# countE.py
# This program reads in a text file and outputs the number of e's it contains.
# Author: Stefania Verduga


# We should import the sys module, which provides access to some variables
# and functions that interact with the Python interpreter.
import sys

if len(sys.argv) < 2: 
    print("Please provide a filename argument.")
    sys.exit()  # function to exit the program in case no argument is entered

filename = sys.argv[1]  # variable argv allows us to access command-line arguments

with open(filename, 'r') as file:
    content = file.read()

count = 0
for char in content:
    if char == 'e' or char == 'E':
        count += 1

print(count)