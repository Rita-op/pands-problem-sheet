# The solution to weekly task 08: Write a program that displays a plot of the functions f(x)=x, g(x)=x^2 
# and h(x)=x^3 in the range [0, 4] on the one set of axes.
# Author: Rita Ortega

# It imports the numpy and matplotlib modules 
import numpy as np
import matplotlib.pyplot as plt

# It is used the arange function of the numpy module to get a range of floating-point numbers between [0,4] to define the x variable
xpoints  = np.arange(0.,4.01,0.01)

# It defines the functions that we need to represent graphically
fpoints = xpoints 
gpoints = xpoints ** 2
hpoints = xpoints ** 3  

# It defines the kind of plot to use as well as certain features of it
plt.plot(xpoints, fpoints, color = "red", label = "f(x)=x", linestyle= "dashdot")
plt.plot(xpoints, gpoints, color = "blue", label = "g(x)=x**2",linestyle= "dashed")
plt.plot(xpoints, hpoints, color = "green", label = "h(x)=x**3", linestyle= "solid")

# It adds a title to the plot with a specified size and font
plt.title("Functions Representation", fontsize= 15.0, fontweight= "bold")

# It adds a legend and a grid to the plot
plt.legend(loc = "upper left", edgecolor='grey', shadow = True )
plt.grid()

# It opens a new window that displays the plot 
plt.show()



"""

REFERENCES:

https://pynative.com/python-range-for-float-numbers/
https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html
https://www.includehelp.com/python/bold-text-label-in-plot.aspx
https://www.geeksforgeeks.org/custom-legends-with-matplotlib/
https://www.w3schools.com/python/matplotlib_grid.asp
https://matplotlib.org/stable/tutorials/introductory/pyplot.html
https://www.w3schools.com/python/matplotlib_pyplot.asp


"""





