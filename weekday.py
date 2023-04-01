# weekday.py
# This program outputs whether or not today is a weekday.
# Author: Stefania Verduga

import datetime

# We need to get the current date and time
x = datetime.datetime.now()
# By default, these calendars have Monday as the first day of the week
# and Sunday as the last day (Monday = 0 and Sunday = 6)
if x.weekday() < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
    