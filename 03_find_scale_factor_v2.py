"""Ask user for number of servings in recipe and
number of servings desired and then calculate the scale factor
Created by Sammy Cummins
Version 2 - uses number checking function to ensure input is a number
10/06/2021
"""


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


# Main routine
# Get serving size
serving_size = float(input("What is the recipe serving size?"))

# Get desired number of servings
desired_size = float(input("How many servings are needed?"))

# Calculate scale factor
scale_factor = desired_size / serving_size

print("Scale factor is {}".format(scale_factor))
