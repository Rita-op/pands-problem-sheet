# The solution to weekly task 02: "Calculate somebody's Body Mass Index (BMI)"
# Author: Rita Ortega

# I found how the Body Mass Index (BMI) is calculated on this website: https://www.calculator.net/bmi-calculator.html


weight = input('Enter your weight (kg):')
height = input('Enter your height (cm):')
heightm = int(height)/100

BMI = int(weight) / (heightm)**2

bmiprint = 'The Body Mass Index (kg/m2) is {:.2f}'
print(bmiprint.format(BMI))

#REFERENCES : https://www.w3schools.com/python/python_string_formatting.asp




