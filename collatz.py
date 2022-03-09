# The solution to weekly task 04: "Write a program that asks the user to input any positive integer and 
# outputs the successive values of the required calculation"
# Author: Rita Ortega

# It creates an empty list
values = []

# It reads the number given and adds it to the list 
intNumber = int(input('Please enter a positive integer:'))
values.append(intNumber) 

# It creates a while loop that performs the calculations required and adds the values to the list until the current value is one
while intNumber != 1:
    if intNumber % 2 == 0:
      intNumber = intNumber // 2  
    else:
      intNumber = (3 * intNumber) + 1 
    values.append(intNumber) 

# It prints out the created list without brackets and separate it by spaces
print(*values, sep = " ") 




"""  

REFERENCES:

https://www.w3schools.com/python/python_while_loops.asp
https://medium.com/the-art-of-python/the-collatz-sequence-in-python-eb7e1f1b4f9e

"""


