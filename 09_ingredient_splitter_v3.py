"""" Further version of an ingredient splitter which splits the ingredients
from one line of input into quantity, unit, and ingredient
Created by Sammy Cummins
Version 3 - Testing on the full recipe
22/06/2021
"""

import re  # This is the Regular Expression module

# Reading from a full list of ingredients
# Ingredient has mixed fraction followed by unit and ingredient
full_recipe = [
    "1 1/2 ml flour",
    "3/4 cup milk",
    "1 cup flour",
    "2 tablespoons white sugar",
    "1 3/4 cups flour",
    "1.5 tsp baking powder",
    "pinch of cinnamon"
]

# The regex format below is expecting: number <space> number
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"
# \d for a digit, /d{1,3} allows 1-3 digits, /s for space, \/ for divide

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()
    # Get amount
    if re.match(mixed_regex, recipe_line):  # Checking for the mixed fraction
        # Get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()
        # .group returns the part of the string where there was a match

        # Replace the space in the mixed number with '+' sign
        amount = mixed_num.replace(" ", "+")

        # changes the string into a float using python's evaluation method
        amount = eval(amount)

        # Get unit and ingredient
        compile_regex = re.compile(mixed_regex)
        # Compiles the regex into a string object - so we can search for patterns

        unit_ingredient = re.split(compile_regex, recipe_line)
        # Produces the recipe line unit and amount as a list

        unit_ingredient = (unit_ingredient[1]).strip()
        # Removes the extra white space before and after the unit,
        # 2nd element in list, converting it into a string

    else:
        # Splits the line at the first space
        get_amount = recipe_line.split(" ", 1)

        try:
            amount = eval(get_amount[0])  # Convert amount to float if possible
        except NameError:  # NameError rather than ValueError
            amount = get_amount[0]

        unit_ingredient = get_amount[1]

    get_unit = unit_ingredient.split(" ", 1)
    # Splits the string into a list containing just the unit and ingredient
    unit = get_unit[0]  # Making the 1st item in the list 'unit'
    ingredient = get_unit[1]  # Making the 2nd item in the list 'ingredient'

    # All 3 elements of the original recipe line are now broken into 3 required variables
    print("{} {} {}".format(amount, unit, ingredient))
