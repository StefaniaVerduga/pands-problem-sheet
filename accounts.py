# accounts.py
# Author: Stefania Verduga
# This program reads in a 10 character account number
# and outputs the account number with only the last 4 digits showing

# Read in account number
account_num = input("Please enter an account number: ")

# Get the length of the account number
num_digits = len(account_num)

# Depending on the account length, the four last digits will be displayed,
# and we will replace the other digits with 'x'
new_account_num = 'X' * (num_digits - 4) + account_num[-4:]

# Output the new account number
print(new_account_num)