# accounts.py
# Author: Stefania Verduga
# This program reads in a 10 character account number
# and outputs the account number with only the last 4 digits showing

account_num = input("Please enter an account number: ")

num_digits = len(account_num)

# Depending on the account length, the four last digits will be displayed,
# and the other digits will be replaced with 'x'
new_account_num = 'X' * (num_digits - 4) + account_num[-4:]

print(new_account_num)