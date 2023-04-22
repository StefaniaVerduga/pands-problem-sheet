# bank.py
# This program prints out a sum of two money amounts previously inserted
# Author: Stefania Verduga

n1 = int(input("Enter amount 1 (in cent): "))
n2 = int(input("Enter amount 2 (in cent): "))

total_cent = n1 + n2
total_eur = total_cent // 100  # integer division
total_cent = total_cent % 100  # remainder after integer division

print(f"The sum of these is: €{total_eur}.{total_cent:02d}")