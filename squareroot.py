# squareroot.py
# This program takes a positive floating-point number as input
# and outputs an approximation of its square root.
# Author: Stefania Verduga

num = float(input("Please, enter a positive number: "))

# The function sqrt checks if the input number is zero, and returns 0 if it is.
def sqrt(num, tolerance=0.0001):
    if num == 0:
        return 0

    approx = num / 2
    g = approx + 1
    while(abs(approx - g) > tolerance):
        n = num / approx
        g = approx
        approx = (approx + n) / 2

# The function returns the approximate square root rounded to one decimal.
    return round(approx, 1)

print(f"The square root of {num} is approx. {sqrt(num)}")