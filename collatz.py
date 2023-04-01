# collatz.py
# This program ask the user to input any positive integer
# and outputs the value following the criteria:
# If input is even, divide by two
# but, if it is odd, multiply it by three and add one.
# The program will end if the current value is one.
# Author: Stefania Verduga

number = int(input("Please, enter a positive integer: "))
while number != 1:
    print(number,end=" ")
    if number % 2 == 0:
        number = number // 2
    else:
        number = (number * 3) + 1
print(number)