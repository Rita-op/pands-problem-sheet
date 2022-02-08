# The solution to weekly task 03: "Write a program that asks a user to input a string and outputs every second letter in reverse order"
# Author: Rita Ortega

# It reads the sentence given
inputSentece = input('Please enter a sentence: ')

# It selects every second letter of the sentence given
everySecondLetter = inputSentece[1::2]

 # It reverses the previous string (everySecondLetter)
reversedOutput = everySecondLetter[::-1]

# It prints out the result of the reversedOutput variable
print(reversedOutput)


"""

REFERENCES:

https://codippa.com/how-to-print-characters-at-even-position-in-string-in-python/
https://www.w3schools.com/python/python_howto_reverse_string.asp


"""

