"""Ask user for number of servings in recipe and
number of servings desired and then calculate the scale factor
Created by Sammy Cummins
Version 1
10/06/2021
"""

# Get serving size
serving_size = float(input("What is the recipe serving size?"))

# Get desired number of servings
desired_size = float(input("How many servings are needed?"))

# Calculate scale factor
scale_factor = desired_size / serving_size

print("Scale factor is {}".format(scale_factor))
