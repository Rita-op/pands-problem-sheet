# The solution to weekly task 07: "Write a program that reads in a text file and outputs the number of e's it contains"
# Author: Rita Ortega

# It imports the fileinput module that allows us to read the file that is provided as an argument on the command line 
import fileinput
count_letter = 0

# It is used a for loop that reads through each line of the file given on the command line
for line in fileinput.input(mode = "r"):

# This for loop has been used to traverse through the letters in each line
    for letter in line:

# This if statement counts the number of e's the given document contains (uppercase and lowercase)
      if (letter == "e" or letter == "E"):
       count_letter = count_letter + 1 

# It prints out the number of e's the given document contains
print (count_letter)




"""

REFERENCES:

https://stackoverflow.com/questions/7033987/get-a-file-from-cli-input
https://docs.python.org/3/library/fileinput.html
https://www.codespeedy.com/count-occurrence-of-character-in-file-using-python/
https://www.sanfoundry.com/python-program-read-file-counts-number/


"""
