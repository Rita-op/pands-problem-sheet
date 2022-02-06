# The solution to weekly task 03: "Write a program that asks a user to input a string and outputs every second letter in reverse order"
# Author: Rita Ortega


inputSentece = input('Please enter a sentence: ')
splitted_inputSentence = inputSentece[1::2]
finalOutput = splitted_inputSentence[::-1]

print(finalOutput)



"""

REFERENCES:
https://stackoverflow.com/questions/46503865/getting-every-nth-character-in-the-string-in-python
https://codippa.com/how-to-print-characters-at-even-position-in-string-in-python/
https://www.w3schools.com/python/python_howto_reverse_string.asp


"""

