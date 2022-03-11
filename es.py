# The solution to weekly task 07: "Write a program that reads in a text file and outputs the number of e's it contains"
# Author: Rita Ortega


import fileinput
countLetter = 0

for line in fileinput.input(mode = "r"):
    for letter in line:
      if (letter == "e" or letter == "E"):
       countLetter = countLetter + 1 
print (countLetter)




"""

REFERENCES:

https://stackoverflow.com/questions/7033987/get-a-file-from-cli-input
https://docs.python.org/3/library/fileinput.html
https://www.codespeedy.com/count-occurrence-of-character-in-file-using-python/
https://www.sanfoundry.com/python-program-read-file-counts-number/


"""
