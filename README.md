# ATU Galway - Programming and Scripting

Course: HDip in Computer in Data Analytics  
Module: Programming and Scripting  
Author: Stefania Verduga  

The "pands-problem-sheet" repository contains the solutions of different weekly tasks within the Programming and Scripting module.

## Table of Contents

<!-- toc -->

1. [Week 01: helloworld.py] (#week-01:-helloworld.py)
2. [Week 02: bank.py] (#week-02:-bank.py)
3. [Week 03: accounts.py] (#week-03:-accounts.py)
4. [Week 04: collatz.py] (#week-04:-collatz.py)
5. [Week 05: weekday.py] (#week-05:-weekday.py)
6. [Week 06: squareroot.py] (#week-06:-squareroot.py)
7. [Week 07: countE.py] (#week-07:-countE.py)
8. [Week 08: plottask.py] (#week-08:-plottask.py) 

<!-- tocstop -->
___

## Week 01: helloworld.py
#### Task description

This program is a simple program that prints the message "Hello World" to the console or terminal.

#### Program explanation

```http
print("Hello World!")
```
The "print()" function is a built-in function in Python that outputs the specified message to the console. In this case, the message is the string "Hello World".

___

## Week 02: bank.py
#### Task description

This program prompts the user to enter two amounts in cents and then converts them to euros by dividing by 100. The sum of the two amounts in euros is then printed using a formatted string.

#### Program explanation

This lines, prompts the user to enter two amounts in cents and reads them as inputs. It then converts the inputs to integers using the int() function and assigns them to the variables "n1" and "n2".
```http
n1 = int(input("Enter amount 1 (in cent): "))
n2 = int(input("Enter amount 2 (in cent): "))
```
The next lines, converts the inputs from cents to euros by dividing it by 100 and assigns the results to new variables called "n1eur" and "n2eur".
```http
n1eur = n1 / 100
n2eur = n2 / 100
```
Finally, the result of the two amounts in euro is printed, using a formatted string.
```http
print(f"The sum of these is: €{n1eur + n2eur}")
```

#### References
- String format: [https://realpython.com/python-f-strings/]

___

## Week 03: accounts.py
#### Task description

This program reads in a 10 character account number and outputs the account number with only the last 4 digits being visible.

#### Program explanation

The following line prompts the user to enter a 10-digit account number and reads it as string input, which is then assigned to the variable "account".
```http
account = input("Pease enter a 10 digit account number: ")
```
In the next block of code, a new variable is created, "account1" which will be used to replace the first six digits of the original account number.
The variable "account2" extracts the last four digits of the original account number using slicing notation The "[-4:]" slice indicates that we want the last four characters of the string, and the colon : indicates that we want to select all characters from the fourth last character to the end of the string. 
The variable "account3" concatenates the string "account1" with the string "account2". The result is a string with the first six digits replaced with "x" characters and the last four digits remaining the same.
```http
account1 = "xxxxxx"
account2 = account[-4:]
account3 = account1 + account2
```
The output will be a string with "xxxxxx" as the first six characters and the last four characters equal to the last four characters of the original account number entered by the user.
```http
print(account3)
```

#### Notes
This program has limitations, as it will not be valid for accounts with more than 10 digits.

#### References
- Slicing in python: [https://www.w3schools.com/python/ref_func_slice.asp#:~:text=The%20slice()%20function%20returns,slice%20only%20every%20other%20item.]

___


## Week 04: collatz.py
#### Task description

This program asks the user to input any positive integer and outputs the value, following the criteria: if the input is even, it will be divided by two but, if it is odd, it will be multiplied by three and added one. The program will end if the current value is one.

#### Program explanation

The user should input a positive integer which is assigned to the variable "number" as an integer. 
```http
number = int(input("Please, enter a positive integer: "))
```
It then enters a while loop that runs as long as the value of 'number' is not equal to 1.
Within the loop, the current value of 'number' is printed to the screen using the 'print' function. The 'end' parameter is set to a space character, which means that each printed value will be separated by a space.
Next, an if-else statement checks if the value of 'number' is even by checking if the remainder of 'number' divided by 2 is zero. If it is even, then the value of 'number' is divided by 2 using integer division (//) and the result is assigned back to 'number'. If it is odd, then the value of 'number' is multiplied by 3 and then added to 1, and the result is assigned back to 'number'.
```http
while number != 1:
    print(number,end=" ")
    if number % 2 == 0:
        number = number // 2
    else:
        number = (number * 3) + 1
```
Finally, after the while loop completes, the last value of 'number' is printed to the screen using the 'print' function. If the initial input was a power of 2, then the while loop will only run once and the initial value will be printed followed by 1. Otherwise, the loop will continue to run until the value of 'number' eventually becomes 1, at which point it will be printed as the last value.
```http
print(number)
```

#### References
- Print without new line: [https://www.geeksforgeeks.org/print-without-newline-python/]
