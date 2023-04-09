# ATU Galway - Programming and Scripting

Course: HDip in Computer in Data Analytics  
Module: Programming and Scripting  
Author: Stefania Verduga  

The "pands-problem-sheet" repository contains the solutions of different weekly tasks within the Programming and Scripting module.

## Table of Contents


1. [Week 01 - helloworld.py](#week-01---helloworld.py)
2. [Week 02 - bank.py](#week-02---bank.py)
3. [Week 03 - accounts.py](#week-03---accounts.py)
4. [Week 04 - collatz.py](#week-04---collatz.py)
5. [Week 05 - weekday.py](#week-05---weekday.py)
6. [Week 06 - squareroot.py](#week-06---squareroot.py)
7. [Week 07 - countE.py](#week-07---countE.py)
8. [Week 08 - plottask.py](#week-08---plottask.py) 

___

## Week 01 - helloworld.py
#### Task description

This program is a simple program that prints the message "Hello World" to the console or terminal.

#### Program explanation

```
print("Hello World!")
```
The "print()" function is a built-in function in Python that outputs the specified message to the console. In this case, the message is the string "Hello World".

___

## Week 02 - bank.py
#### Task description

This program prompts the user to enter two amounts in cents and then converts them to euros by dividing by 100. The sum of the two amounts in euros is then printed using a formatted string.

#### Program explanation

This lines, prompts the user to enter two amounts in cents and reads them as inputs. It then converts the inputs to integers using the int() function and assigns them to the variables "n1" and "n2".
```
n1 = int(input("Enter amount 1 (in cent): "))
n2 = int(input("Enter amount 2 (in cent): "))
```
The next lines, converts the inputs from cents to euros by dividing it by 100 and assigns the results to new variables called "n1eur" and "n2eur".
```
n1eur = n1 / 100
n2eur = n2 / 100
```
Finally, the result of the two amounts in euro is printed, using a formatted string.
```
print(f"The sum of these is: €{n1eur + n2eur}")
```

#### References
- String format: [https://realpython.com/python-f-strings/]

___

## Week 03 - accounts.py
#### Task description

This program reads in a 10 character account number and outputs the account number with only the last 4 digits being visible.

#### Program explanation

The following line prompts the user to enter a 10-digit account number and reads it as string input, which is then assigned to the variable "account".
```
account_num = input("Please enter an account number: ")
```
In the next block of code, the program calculates the length of the account number using the len() function and stores it in the variable "num_digits".

A new variable "new_account_num" is created by concatenating the appropriate number of Xs (i.e., the length of the original account number minus 4) and the last 4 digits of the original account number. This is done using the * operator to create a string of Xs of the appropriate length, and the [-4:] slice notation to extract the last 4 digits of the original account number.
```
num_digits = len(account_num)
new_account_num = 'X' * (num_digits - 4) + account_num[-4:]
```
The output will be a string with "Xs" depending on the length of the account plus the four last visible digits.
```
print(new_account_num)
```

#### References
- Slicing in python: [https://www.w3schools.com/python/ref_func_slice.asp#:~:text=The%20slice()%20function%20returns,slice%20only%20every%20other%20item.]
- Length in python: [https://www.w3schools.com/python/gloss_python_string_length.asp]
- Python string concatenation: [https://www.w3schools.com/python/gloss_python_string_concatenation.asp]

___


## Week 04 - collatz.py
#### Task description

This program asks the user to input any positive integer and outputs the value, following the criteria: if the input is even, it will be divided by two but, if it is odd, it will be multiplied by three and added one. The program will end if the current value is one.

#### Program explanation

The user should input a positive integer which is assigned to the variable "number" as an integer. 
```
number = int(input("Please, enter a positive integer: "))
```
It then enters a while loop that runs as long as the value of 'number' is not equal to 1.
Within the loop, the current value of 'number' is printed to the screen using the 'print' function. The 'end' parameter is set to a space character, which means that each printed value will be separated by a space.

Next, an if-else statement checks if the value of 'number' is even by checking if the remainder of 'number' divided by 2 is zero. If it is even, then the value of 'number' is divided by 2 using integer division (//) and the result is assigned back to 'number'. If it is odd, then the value of 'number' is multiplied by 3 and then added to 1, and the result is assigned back to 'number'.
```
while number != 1:
    print(number,end=" ")
    if number % 2 == 0:
        number = number // 2
    else:
        number = (number * 3) + 1
```
Finally, after the while loop completes, the last value of 'number' is printed to the screen using the 'print' function. If the initial input was a power of 2, then the while loop will only run once and the initial value will be printed followed by 1. Otherwise, the loop will continue to run until the value of 'number' eventually becomes 1, at which point it will be printed as the last value.
```
print(number)
```

#### References
- Print without new line: [https://www.geeksforgeeks.org/print-without-newline-python/]
- Python while loops: [https://www.w3schools.com/python/python_while_loops.asp]
- Conditional statement in Python: [https://realpython.com/python-conditional-statements/]

___


## Week 05 - weekday.py
#### Task description

This is a Python program that uses the datetime module to get the current date and time and check whether it is a weekday or the weekend. 

#### Program explanation

The program imports the datetime module using the import statement and gets the current date and time by calling the datetime.datetime.now() function and storing the result in the variable "x".
```
import datetime
x = datetime.datetime.now()
```
The program uses the weekday() method of the "datetime" object "x" to determine which day of the week it is. This method returns an integer between 0 (Monday) and 6 (Sunday), representing the day of the week.

The program checks whether the day of the week is less than 5 (i.e., Monday to Friday), using the "if" statement. If it is, the program prints the string "Yes, unfortunately today is a weekday." to the console. Otherwise, the program prints the string "It is the weekend, yay!" to the console.
```
if x.weekday() < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
```

#### References
- Datetime Python: [https://docs.python.org/3/library/datetime.html]
[https://www.w3schools.com/python/python_datetime.asp]
- Weekday function in Python: [https://www.geeksforgeeks.org/weekday-function-of-datetime-date-class-in-python/]
- Conditional Statement in Python: [https://realpython.com/python-conditional-statements/]

___


## Week 06 - squareroot.py
#### Task description

This program takes a positive floating-point number as input and outputs an approximation of its square root.

#### Program explanation

The program prompts the user to enter a positive number using the input() function and stores the result in the variable "num".
```
num = float(input("Please, enter a positive number: "))
```
The program defines a function called "sqrt" that takes one argument "num".

The "sqrt" function checks if the input number "num" is zero, and returns 0 if it is using the if statement.
If the input number is not zero, the "sqrt" function calculates the approximate square root of the input number using the Babylonian method (Babylonian method for square root is derived from the Newton-Raphson method). The Babylonian method involves taking an initial guess (in this case, "approx = num / 2") and then iteratively refining the guess using the formula "(approx + num / approx) / 2".

The "sqrt" function uses a "while" loop to refine the guess until the guess and the previous guess are within a certain tolerance of each other. In this case, the program compares the current guess with the previous guess and continues iterating until they are equal, which indicates that the approximation has converged.
```
def sqrt(num):
    if num == 0:
        return 0

    approx = num / 2
    g = approx + 1
    while(approx != g):
        n = num / approx
        g = approx
        approx = (approx + n) / 2
```
Once the approximation has converged, the sqrt function returns the approximate square root rounded to one decimal place using the round() function.
```
return round(approx, 1)
```
Finally, the program calls the sqrt function with the user's input number as an argument and prints the result to the console using an f-string.
```
print(f"The square root of {num} is approx. {sqrt(num)}")
```

#### References
- Square root using Babylonian Method: [https://www.w3resource.com/python-exercises/math/python-math-exercise-18.php]
[https://www.geeksforgeeks.org/square-root-of-a-perfect-square/]
- Newton Method for square root: [https://www.geeksforgeeks.org/program-for-newton-raphson-method/]

___


## Week 07 - countE.py
#### Task description

This program reads a file specified in the command-line argument, and counts the number of occurrences of the letter 'e' or 'E' in the file.

#### Program explanation

We need to import the sys module, which provides access to some variables and functions that interact with the Python interpreter.
```
import sys
```
The variable argv allows us to access command-line arguments.
```
filename = sys.argv[1]
```
This block of code allows us to open the specified file by 'filename' in read-only mode. 
It also reads the contents of the file and assigns it to the variable "content".
```
with open(filename, 'r') as file:
    content = file.read()
```
The next line initializes a variable count to 0, which will be used to keep track of the number of 'e' or 'E' characters in the file.
We use a for loop to iterate over every character in the string content and check if the current character is either 'e' or 'E', and if so, increment the count variable.
```
for char in content:
    if char == 'e' or char == 'E':
        count += 1
```
Finally, the program prints the final value of the count variable, which represents the number of occurrences of the letter 'e' or 'E' in the file.
```
print(count)
```

#### References
- Command line arguments in Python: [https://realpython.com/python-command-line-arguments/]
- Sys and sys.argv in Python: [https://docs.python.org/3/library/sys.html#sys.argv]
[https://www.geeksforgeeks.org/python-sys-module/]
[https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/]
- With Statement in Python: [https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/]
- Open file in Python: [https://www.w3schools.com/python/python_file_open.asp]

___


## Week 08 - plottask.py
#### Task description

This program displays: a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2; and a plot of the function h(x)=x^3 in the range [0, 10].

#### Program explanation

The first two lines import NumPy and Matplotlib libraries, respectively. In this program, the numpy library is used to generate random values from a normal distribution, and the matplotlib.pyplot module is used to create the histogram and plot.
```
import numpy as np
import matplotlib.pyplot as plt
```
The program uses the np.random.normal() function from the NumPy library to generate a random sample of 1000 data points from a normal distribution with a mean of 5 and a standard deviation of 2.

The np.random.normal() function takes three arguments:

loc (location) - the mean of the distribution.
scale - the standard deviation of the distribution.
size - the size of the sample to generate.
In this case, the generated sample will have a mean of 5 and a standard deviation of 2. The size parameter is set to 1000, which means that the generated sample will have 1000 data points.

The generated sample is then stored in the variable data, which is used later to create the histogram.
```
mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)
```
It then creates a figure and axes object using Matplotlib's subplots() function. 
The plt.subplots() method returns a tuple containing a figure object and an array of axes objects. The figure object is the top-level container for all the plot elements, while each axes object represents an individual plot within the figure.

- "fig" is a variable that stores the figure object.
- "ax" is a variable that stores the axes object.
- In this case, the plt.subplots() method is called with no arguments, which creates a single subplot.
```
fig, ax = plt.subplots()
```
A histogram is created using Matplotlib's hist() function on the generated data, with the number of bins set to 15, alpha value set to 0.5, and label set to 'Normal Distribution'.

The ax variable is an instance of the Matplotlib Axes class, which represents the drawing area for a single plot. The ax.hist() method takes the following parameters:

x: The data to be plotted.
bins: The number of bins to use in the histogram.
alpha: The transparency level of the bars in the histogram.
label: The label for the histogram in the legend.

In the context of the Matplotlib hist() function, bins refers to the number of bins or intervals in which the data is divided for creating the histogram.

In this program, bins=15 means that the histogram will be divided into 15 equally spaced bins or intervals. Increasing the number of bins can make the histogram more detailed and help reveal patterns in the data, while decreasing the number of bins can make the histogram more general and easier to read.

In the context of the hist() function, alpha refers to the transparency of the bars in the histogram. The alpha value can range from 0 to 1, where 0 means completely transparent and 1 means completely opaque.
In this program, alpha=0.5 means that the bars in the histogram will be semi-transparent, which can help to distinguish overlapping bars and make the plot more visually appealing.
```
ax.hist(data, bins=15, alpha=0.5, label='Normal Distribution')
```
A plot of the function x^3 is created using Matplotlib's plot() function on an array of x values created using NumPy's linspace() function, with the label set to 'x^3'.

The linspace() function creates an array of evenly spaced numbers over a specified interval. In this case, the function is called with the arguments (0, 10, 100), which creates an array of 100 numbers between 0 and 10 (inclusive).
The program uses the generated x values to create a y array for a cubic function. The ** operator is used to raise each x value to the power of 3, generating a cubic function.

Then, the program adds a line plot of the x and y arrays to the existing histogram using the ax.plot() method. The ax.plot() method takes the x and y arrays as the first and second arguments, respectively.
The "color" parameter sets the color of the line to red, while the "linewidth" parameter sets the width of the line to 2. The "label" parameter sets the label of the line in the legend to 'x^3'.
```
x = np.linspace(0, 10, 100)
y = x**3
ax.plot(x, y, color='red', linewidth=2, label='x^3')
```
The axes labels and title are set using the ax.set_xlabel(), ax.set_ylabel(), and ax.set_title() functions.
These methods take string arguments, which are used to set the title of the plot, the x-axis and y-axis labels, respectively.
```
ax.set_title('Histogram and plot')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
```
A legend is added to the plot using Matplotlib's legend() function.
The legend displays the label of each plot on the graph. In this case, the legend displays the label 'Normal Distribution' for the histogram and the label 'x^3' for the line plot.
```
ax.legend()
```
Finally, the plot is displayed using Matplotlib's show() function.
```
plt.show()
```
![HISTOGRAM AND PLOT](/Users/stefania/Pands/pands-problem-sheet/Figure_1.png)

#### References
- Numpy in Python: [https://www.w3schools.com/python/numpy/numpy_getting_started.asp#:~:text=NumPy%20as%20np,referring%20to%20the%20same%20thing.&text=Now%20the%20NumPy%20package%20can,as%20np%20instead%20of%20numpy%20.]
- Matplotlib in Python: [https://matplotlib.org/stable/api/matplotlib_configuration_api.html]
[https://matplotlib.org/stable/api/pyplot_summary.html#]
- Python Histogram plotting: [https://realpython.com/python-histograms/]
[https://python-charts.com/es/distribucion/histograma-matplotlib/]
- Normal Distribution in Python: [https://www.w3schools.com/python/numpy/numpy_random_normal.asp]