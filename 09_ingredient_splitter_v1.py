"""" Initial version of an ingredient splitter which splits the ingredients
from one line of input into quantity, unit, and ingredient
Created by Sammy Cummins
Version 1
22/07/2021
"""

import re  # This is the Regular Expression module

# Ingredient has mixed fraction followed by unit and ingredient
recipe_line = "1 1/2 ml flour"  # Changed to input statement in due course

# The regex format below is expecting: number <space> number
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"
# \d for a digit, /d{1,3} allows 1-3 digits, /s for space, \/ for divide

# Testing to see if the recipe line matches the regular expression
if re.match(mixed_regex, recipe_line):
    print("true")
else:
    print("false")
