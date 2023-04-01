# squareroot.py
# This program takes a positive floating-point number as input
# and outputs an approximation of its square root.
# Author: Stefania Verduga

# num = float(input("Please, enter a positive number: "))

def sqrt(num):
    if num == 0:
        return 0
    else:
        approx = num / 2
        while True:
            better = (approx + num / approx) / 2
            if abs(better - approx) < 0.001:
                return round(better, 1)
            approx = better

# print(f"The square root of {num} is approx. {sqrt(num)}")

num = float(input("Please, enter a positive number: "))

def sqrt(num):
    if num == 0:
        return 0

    g = num / 2
    g2 = g + 1
    while(g != g2):
        n = num / g
        g2 = g
        g = (g + n) / 2

    return round(g, 1)

print(f"The square root of {num} is approx. {sqrt(num)}")