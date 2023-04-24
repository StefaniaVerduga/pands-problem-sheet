# weekday.py
# This program outputs whether or not today is a weekday.
# Author: Stefania Verduga

import datetime

# Need to get the current date and time
x = datetime.datetime.now()
# Monday = 0 and Sunday = 6
if x.weekday() < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
    