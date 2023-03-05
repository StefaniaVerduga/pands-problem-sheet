# accounts.py
# Author: Stefania Verduga
# This program reads in a 10 character account number
# and outputs the account number with only the last 4 digits showing

account = input("Pease enter a 10 digit account number: ")
account1 = "xxxxxx"
account2 = account[-4:]
account3 = account1 + account2
print(account3)