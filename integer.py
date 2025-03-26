#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-03-25

# Tells the user whether the integer is zero, positive or negative.

import random


def main():
    # Greeting message
    print("Greetings! Please input a number")
    user_input = input("Please enter a number: ")
    # Checks if number is positive, negative or zero
    number = float(user_input)
    # Calculates if integer is negative
    if number < 0:
        print("The integer is a negative number")
    # Calculates if the integer is positive
    elif number > 0:
        print("The integer is a positive number")
    # If number is not negative or positive, it is zero
    else:
        print("the number is zero")


if __name__ == "__main__":
    main()
