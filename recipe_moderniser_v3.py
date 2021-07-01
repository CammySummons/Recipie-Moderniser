"""Recipe moderniser - full working program (version 3)
Incorporates ingredients list (component 4)
Created by Sammy Cummins
Version 3
23/06/2021
"""

# Modules to be used
import csv
import re


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


# Number checking function
# Get's the scale factor - which must be a number
def num_check(question):
    error = "You must enter a number more than 0"
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


def get_scale_factor():
    keep_scale_factor = False
    while not keep_scale_factor:

        # Get serving size and checking it is a number
        serving_size = num_check("What is the recipe serving size? ")
        # Get desired number of servings  and checking it is a number
        desired_size = num_check("How many servings are needed? ")
        # Calculate scale factor
        scale_factor = desired_size / serving_size

        # Warn the user if the scale factor is less than .25 or more than 4
        if scale_factor < .25:
            print("Scale factor is {}".format(scale_factor))
            print("Warning: This scale factor is very small and you\n"
                  "might struggle to accurately weigh the ingredients.\n"
                  "Please consider using a larger scale factor and freezing the "
                  "left-overs.")
            change_scale_factor = input("Press <Enter> to keep it, or <any other "
                                        "key> + <enter> to change  ")
            if not change_scale_factor:
                keep_scale_factor = True

        elif scale_factor > 4:
            print("Scale factor is {}".format(scale_factor))
            print("Warning: This scale factor is quite large so you\n"
                  "might have issues with mixing bowl volumes and oven space.\n"
                  "Please  consider using a smaller scale factor and making more than one batch.")
            change_scale_factor = input("Press <Enter> to keep it, or <any other key> + <enter> to change  ")
            if not change_scale_factor:
                keep_scale_factor = True
        else:
            keep_scale_factor = True

    return scale_factor


# Function to get (and check) amount, unit and ingredient
def get_all_ingredients():
    ingredient_list = []  # Set up ingredient list
    valid_list = False
    while not valid_list:
        # Calls the not_blank function and provides the question
        ingredient_name = not_blank("\nEnter ingredient on one line - qty, "
                                    "unit, then name (or 'X' to exit):): \n",
                                    "Ingredient can't be blank",
                                    True).title()
        if ingredient_name != "X":  # Check for escape code
            ingredient_list.append(ingredient_name)  # If exit code not entered,
            # add ingredient to list
        else:
            if len(ingredient_list) < 2:  # Check that list contains 2 items
                print("Please enter at least two ingredients")
            else:
                valid_list = True  # If list contains 2 items break out of loop
                return ingredient_list  # Output list




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
# Calculate scale factor
scale_factor = get_scale_factor()


# Get ingredients
full_recipe = get_all_ingredients()
print(full_recipe)

# Loop for each ingredient...
# Get ingredient amount
# Scale amount using scale factor
# Get ingredient name and check it's not blank and doesn't contain numbers
# Get unit
# Convert to ml
# Convert from ml to g
# Add updated ingredient to list

# Output modernised recipe
