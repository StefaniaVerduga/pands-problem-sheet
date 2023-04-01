# squareroot.py
# This program takes a positive floating-point number as input
# and outputs an approximation of its square root.
# Author: Stefania Verduga

num = float(input("Please, enter a positive number: "))

# The function sqrt checks if the input number is zero, and returns 0 if it is.
def sqrt(num):
    if num == 0:
        return 0

# If the input is different to 0, it calculates the approximate value for the square root,
# by dividing the input number by 2 and aplying a mathematical formula.
# This formula involves taking the average of the current approximate value and the input number divided by the current approximate value.
    approx = num / 2
    g = approx + 1
    while(approx != g):
        n = num / approx
        g = approx
        approx = (approx + n) / 2

# The function returns the approximate square root rounded to one decimal.
    return round(approx, 1)

print(f"The square root of {num} is approx. {sqrt(num)}")