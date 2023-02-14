# bank.py
# This program prints out a sum of two money amounts previously inserted
# Author: Stefania Verduga

n1 = int(input("Enter amount 1 (in cent): "))
n2 = int(input("Enter amount 2 (in cent): "))
n1eur = n1 / 100
n2eur = n2 / 100
print(f"The sum of these is: €{n1eur + n2eur}")