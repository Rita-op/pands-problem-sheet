# The solution to weekly task 05: "Write a program that outputs whether or not today is a weekday"
# Author: Rita Ortega

# Imports the library calendar to obtain what day it is today
from datetime import date
import calendar
current_date = date.today()

# It gets the name of the day by using the day_name array from the calendar library taking into account what day it is today (currentDate)
day_name = calendar.day_name[current_date.weekday()]

# It prints out the message "Yes, unfortunately is a weekday" in case today is a weekday
if (day_name == "Monday"
    or day_name == "Tuesday"
    or day_name == "Wednesday"
    or day_name == "Thursday"
    or day_name == "Friday"):

 print("Yes, unfortunately today is a weekday.")

# It prints out the message "It is a weekend, yay!" in case today is the weekend
else:
 print("It is the weekend, yay!")



"""

REFERENCES:

https://www.delftstack.com/howto/python/python-datetime-day-of-week/#:~:text=of the day.-,Use the weekday() Method to Get the Name of,0 and Sunday is 6
https://pythonexamples.org/python-if-or/
 

"""
