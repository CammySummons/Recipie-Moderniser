"""Get recipe from user, checking that input doesn't contain
numbers and is not left blank
Created by Sammy Cummins
version 1 08/06/2021
"""

# Ask user for recipe name
recipe_name: str = input("What is the recipe name?")

# Error message - in the event of blank or contains digits
error = "Your recipe is blank or has numbers in it!"

# Check each character in the recipe name and find any numbers
contains_number = False
for letter in recipe_name:
    if letter.isdigit():
        contains_number = True

# Print error message if recipe_name is blank or contains digits
if not recipe_name or contains_number:
    print(error)
else:
    print("Recipe name is OK")
