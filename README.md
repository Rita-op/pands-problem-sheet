# pands-problem-sheet


## This repository contains the solutions to the weekly task problems of the module: " Programming and Scripting"


-----------

## FILE : bmi.py 


The solution to week 02

This file contains the solution to weekly task 02. In this task, we were told to calculate someone's Body Mass Index (BMI).

REFERENCES:
- Website used to find how to calculate a BMI: https://www.calculator.net/bmi-calculator.html
- How to print the Body Mass Index's result as a number with two decimals: https://www.w3schools.com/python/python_string_formatting.asp 


-----------

## FILE: secondstring.py


The solution to week 03

This file contains the solution to weekly task 03. In this task, we needed to write a program that asks a user to input a string and outputs every second letter in reverse order. 

REFERENCES:
- Learn how to reverse a String: https://www.w3schools.com/python/python_howto_reverse_string.asp
- Select all the characters at an even position in a string: https://codippa.com/how-to-print-characters-at-even-position-in-string-in-python/


-----------

## FILE: collatz.py


The solution to week 04

 This file contains the solution to weekly task 04. In this task, we were told to write a program that asks the user to input any positive integer number and outputs the successive values of a required calculation. For the case that concerns us, at each step we have to calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. The program has to end if the current value is one.

REFERENCES:
- I got the idea about how to make the collatz program: https://medium.com/the-art-of-python/the-collatz-sequence-in-python-eb7e1f1b4f9e
- How to use while loops: https://www.w3schools.com/python/python_while_loops.asp 
- How to print a list without brackets and separate it by spaces: https://www.adamsmith.haus/python/answers/how-to-print-a-list-without-brackets-in-python#:~:text=Use%20*%20to%20print%20a%20list,set%20sep%20to%20%22%2C%20%22%20 


-----------

## FILE: weekday.py


The solution to week 05

This file contains the solution to weekly task 05. In this task, we needed to write a program that outputs whether or not today is a weekday.

REFERENCES:
- How to obtain what day it is and convert it into the corresponding day of the week: https://www.delftstack.com/howto/python/python-datetime-day-of-week/#:~:text=of%20the%20day.-,Use%20the%20weekday()%20Method%20to%20Get%20the%20Name%20of,0%20and%20Sunday%20is%206
- I got the idea about how to output whether or not today is a weekday using the if statement with or operator: https://pythonexamples.org/python-if-or/


-----------

## FILE: squareroot.py


The solution to week 06

This file contains the solution to weekly task 06. In this task, we needed to write a program that takes a positive floating-point number as input and outputs an approximation of its square root. In order to do that, we could not use any built-in function but we had to create our own function.

As we were advised, I used Newton's Method for estimating square roots to develop my solution. The equation used in the solution, since we needed to calculate the square root of a number, was the following: 

             x1 = 0.5 *(x0 + (n/x0))

REFERENCES:

The following are the websites used to get information about Newton's Method for estimating square roots and how to apply it:
- https://www2.math.upenn.edu/~kazdan/202F09/sqrt.pdf
- https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf

I used the websites shown below to develop my solution to obtain the square root of a number using the Newton's Method:
- https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
- https://www.coursehero.com/tutors-problems/Python-Programming/19731761-Package-Newtons-method-for-approximating-square-roots-Case-Study-Ap/
- https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots

How to print the result as a number with one decimal: 
- https://www.w3schools.com/python/python_string_formatting.asp 


-----------

## FILE: es.py


The solution to week 07


This file contains the solution to weekly task 07. In this task, we were told to write a program that reads in a text file and outputs the number of e's it contains. I would like to point out that I assumed that we are asked to count all the e’s regardless of whether they are in uppercase or lowercase. For that reason, my solution to this weekly task counts all the e's a given document contains (uppercase and lowercase).

Lastly, I let you know that I have included a text file called "moby-dick.txt" that you can use to test the code.

REFERENCES:

I used the websites shown below to develop my solution to take the filename from an argument on the command line:
- https://stackoverflow.com/questions/7033987/get-a-file-from-cli-input
- https://docs.python.org/3/library/fileinput.html

Reading the following websites, I got the idea about how to read in a text file and outputs the number of e's it contains:
- https://www.codespeedy.com/count-occurrence-of-character-in-file-using-python/
- https://www.sanfoundry.com/python-program-read-file-counts-number/

I created my test text file using this website:
- https://archive.org/stream/mobydickorwhale01melvuoft/mobydickorwhale01melvuoft_djvu.txt 


-----------

## FILE: plottask.py


The solution to week 08

This file contains the solution to weekly task 08. In this task, we were told to write a program that displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes.

REFERENCES:

How to get a range of floating-point numbers between [0,4] to define the x variable: 
- https://pynative.com/python-range-for-float-numbers/

I used the websites shown below to make the plot looks nicer:
- https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html
- https://www.includehelp.com/python/bold-text-label-in-plot.aspx
- https://www.geeksforgeeks.org/custom-legends-with-matplotlib/
- https://www.w3schools.com/python/matplotlib_grid.asp
- https://matplotlib.org/stable/tutorials/introductory/pyplot.html

How to use matplotlib.pyplot module: 
- https://www.w3schools.com/python/matplotlib_pyplot.asp


-----------






