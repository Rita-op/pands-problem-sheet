# The solution to weekly task 06: "Write a program that takes a positive floating-point number 
# as input and outputs an approximation of its square root"
# Author: Rita Ortega

# It reads the number given and converts it into a float
n = float(input("Please enter a positive number: ")) 

# It defines the sqrt() function and some variables that we are going to need in our calculations
def sqrt (n):
  precision = 0.00001
  x0 = 1
  x1 = x0

# It creates a while loop in order to apply Newton's Method for estimating square roots that stops when 
# the precision of the estimation is less or equal than the specified (0.00001)
  while abs(n-x1**2) > precision: 
    x0 = x1
    x1 = 0.5 * (x0 + n/x0) 
  return x1

# It uses the function we have defined above to obtain an approximation of the square root of the number given through Newton's Method
result  = sqrt(n)

# It prints out a message with the result of the square root for the number given 
print("The square root of {} is approx. {:.1f}". format(n,result))




"""

REFERENCES:

https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
https://www.coursehero.com/tutors-problems/Python-Programming/19731761-Package-Newtons-method-for-approximating-square-roots-Case-Study-Ap/
https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots


"""