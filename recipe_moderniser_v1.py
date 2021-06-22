""" Recipe moderniser - full working program
Gets recipe name and recipe source (components 1 and 2)
Created by Sammy Cummins
Version 1 - includes 'To Do' list
21/06/2021
"""

# Modules to be used
import csv


# FUNCTIONS
def not_blank(question, error_msg, num_ok):
    error = error_msg
    valid = False

    while not valid:
        number = False  # Initial assumption - name contains no digits
        response = input(question)

        if not num_ok:  # set to False
            for letter in response:  # Check for digits in recipe name
                if letter.isdigit():  # Tests for True - by default
                    number = True  # Sets true if any digit found

        if not response or number is True:  # generate error for blank name or digits
            print(error)

        else:  # no error found
            return response  # return bypasses the need to set 'valid' to True.

# MAIN ROUTINE

# Set up dictionaries

# Set up list to hold 'modernised' ingredients


# Get recipe name and check it is not blank and contains no numbers
# Customisable error message eg to include mention of numbers
recipe_name = not_blank("What is the recipe name? ",
                        "The recipe name can't be blank, or contain numbers!",
                        False)  # "False" to disallows digits in name


# Get recipe source and check it's not blank - numbers OK
# Customisable error message eg to include mention of numbers
source = not_blank("Where is the recipe from? ",
                   "The recipe source can't be blank!",
                   True)  # "True" allows digits in name


# Get serving sizes and desired number of servings

# Get ingredients
# Loop for each ingredient...
# Get ingredient amount
# Scale amount using scale factor
# Get ingredient name and check it's not blank and doesn't contain numbers
# Get unit
# Convert to ml
# Convert from ml to g
# Add updated ingredient to list

# Output modernised recipe
