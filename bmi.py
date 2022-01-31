# The solution to weekly task 02: "Calculate somebody's Body Mass Index (BMI)"
# Author: Rita Ortega

# I found how the Body Mass Index (BMI) is calculated on this website: https://www.calculator.net/bmi-calculator.html

# It reads the numbers given
weight = input('Enter your weight (kg):')
height = input('Enter your height (cm):')

# It converts the height from string to an integer and from centimeters to meters
height_m = int(height)/100

# It calculates the Body Mass Index with the given values
BMI = int(weight) / (height_m)**2

# It prints out a message with the result of the Body Mass Index calculation with two decimals
bmiprint = 'The Body Mass Index (kg/m2) is {:.2f}'
print(bmiprint.format(BMI))

# REFERENCES : https://www.w3schools.com/python/python_string_formatting.asp




