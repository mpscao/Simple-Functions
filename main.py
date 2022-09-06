# NAME: Darren Cao
# ID: 2489322953
# DATE: 2022-09-05
# DESCRIPTION: <Code that will perform 8 tasks using user-created functions.>

import math


# Task 1
# Complete function double so that it takes a number and returns twice its value
# according to the examples in the docstring. Use a return statement; note that
# this function does not have a print statement.
def double(num: float) -> float:

 
    dub = num * 2 # double the number entered
    return dub


# Task 2
# Function our_maximum takes two numbers and returns the larger of the two.
# Complete the function.
def our_maximum(num1: float, num2: float) -> float:

 
    maximum = max(num1, num2) # find maxximum of two numbers
    return maximum
  


# Task 3
# Complete the following function.
def max_of_min(num1: float, num2: float, value1: float, value2: float) -> float:

  
    min1 = min(num1, num2) # find the minimum of the first two numbers entered
    min2 = min(value1, value2) # find minimum of next two numbers entered
    maxi_of_mini = max(min1, min2) # find maximum of the two minimums found
    return maxi_of_mini



# Task 4
# Function format_name receives two parameters.
# The first parameter represents a first name and the second represents a last name.
# It returns a string in the format: last_name, first_name
# where last_name and first_name are replaced by the given last and first names.
def format_name(first_name: str, last_name: str) -> str:
    """ Return a string in format last_name, first_name.
    >>> format_name('John', 'Smith')
    'Smith, John'
    """
    name = (last_name + ", " + first_name) # string that starts with last name then ',', then first name
    return name
    pass


# Task 5
# Complete the following function circle_area.
# It receives the radius and returns the area of the circle.
# Add proper comments.
def circle_area(radius: float) -> float:

    area = (math.pi * (radius ** 2)) # area of circle is pi times (radius squared),
    return area



# Task 6
# Function sum_to receives one parameter
# the parameter is a number
# returns an integer value: the sum of all integers from 1 to that number
# Add proper comments.

def sum_to(n: int) -> int:
    sum = 0 # set sum initially to 0 so sum is an int that can be initially added to 1
    # for loop that iterates from 1 to n
    for i in range(n + 1):
        sum += i # add the integer each time to the sum
    return sum



# Task 7
# Complete function is_odd which receives one parameter.
# the parameter is a number.
# returns a boolean value True if the number is odd and False otherwise.
# Add proper comments.
def is_odd(n: int) -> bool:
    # if statement to return true if the integer is odd
    if(n % 2 == 1):
        return True
    # else if the integer is even return false
    elif(n % 2 == 0):
        return False



# Task 8
# Complete function is_even which receives one parameter.
# the parameter is a number.
# returns a boolean value True if the number is even and False otherwise.
def is_even(n: int) -> bool:
    # if statement to return true if the integer is even
    if (n % 2 == 0):
        return True
    # else if the integer is odd return false
    elif (n % 2 == 1):
        return False



# Complete calling
def main():
    print("Starting task 1, doubling a number.")
    num_to_double = input("Please enter the number you would like to duplicate: ")
    print("Double of", num_to_double, "is", double(float(num_to_double)))
    input("Press any key to continue...\n")

    print("Starting task 2, finding maximum.")
    first_num = input("Please enter the first number: ")
    second_num = input("Please enter the second number: ")
    print("Max of", first_num, "and", second_num, "is", our_maximum(float(first_num), float(second_num)))
    input("Press any key to continue...\n")

    print("Starting task 3, finding max of min.")
    user_num1 = input("Please enter the a value for num1: ")
    user_num2 = input("Please enter the a value for num2: ")
    user_value1 = input("Please enter the a value for value1: ")
    user_value2 = input("Please enter the a value for value2: ")
    print("Max of min of pairs (" + user_num1 + "," + user_num2 + ") and (" +
          user_value1 + "," + user_value2 + ") is ",
          max_of_min(float(user_num1), float(user_num2), float(user_value1), float(user_value2)))
    input("Press any key to continue...\n")

    print("Starting task 4, format name.")
    first_num = input("Please enter the first name: ")
    second_num = input("Please enter the last name: ")
    print(format_name(first_num, second_num))
    input("Press any key to continue...\n")

    print("Starting task 5, finding area of circle.")
    rad = input("Please enter a value for radius: ") # to set a variable for radius of circle
    print(circle_area(float(rad))) # to print the area of circle using the inputted radius
    input("Press any key to continue...\n")
   

    print("Starting task 6, finding Summation of n.")
    to_sum_up_to = input("Please enter the number you'd like to sum up to: ")
    print("Summing up to ", to_sum_up_to, "yields", sum_to(int(to_sum_up_to)))
    input("Press any key to continue...\n")

    print("Starting task 7 checking odd:")
    user_input = input("Please enter the number you'd like to check: ")
    print("It is", is_odd(float(user_input)), "that", user_input, "is odd.")
    input("Press any key to continue...\n")

    print("Starting task 8 checking even:")
    user_even = input("Please enter the number you'd like to check: ") # to set variable for number we're looking at
    print("It is", is_even(float(user_even)), "that", user_even, "is even.") # to print if number inputted is even
    input("Press any key to end...\n")



# Do not change
if __name__ == "__main__":
    main()
