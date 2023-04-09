# plottask.py
# This program displays: a histogram of a normal distribution 
# of a 1000 values with a mean of 5 and standard deviation of 2;
# and a plot of the function h(x)=x^3 in the range [0, 10]
# Author: Stefania Verduga

import numpy as np
import matplotlib.pyplot as plt

# Generate data for normal distribution
mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)

# Create a figure and axes object
fig, ax = plt.subplots()

# Create histogram
ax.hist(data, bins=15, alpha=0.5, label='Normal Distribution')

# Create plot of x^3
x = np.linspace(0, 10, 100)
y = x**3
ax.plot(x, y, color='red', linewidth=2, label='x^3')

# Set plot title and labels
ax.set_title('Histogram and plot')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

# Add legend
ax.legend()

# Show plot
plt.show()