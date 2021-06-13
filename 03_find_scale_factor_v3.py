"""Ask user for number of servings in recipe and
number of servings desired and then calculate the scale factor
Created by Sammy Cummins
Version 3 - Get's he scale factor and warns if it is too large or too small
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
keep_scale_factor = False
while not keep_scale_factor:

    # Get serving size
    serving_size = float(input("What is the recipe serving size?"))

    # Get desired number of servings
    desired_size = float(input("How many servings are needed?"))

    # Calculate scale factor
    scale_factor = desired_size / serving_size

    # Warn user if the scale factor  is less than 0.25 or more than 4
    if scale_factor < .25:
        print("Scale factor is {}".format(scale_factor))
        print("Warning: This scale factor is very small and you\n"
              "might struggle to accurately weigh the ingredients. \n"
              "Please consider using a larger scale factor and freezing the"
              "left-overs.")
        change_scale_factor = input("Press <Enter> to keep it, or <any other "
                                    "key> + <Enter> to change ")
        if not change_scale_factor:
            keep_scale_factor = True

    elif scale_factor > 4:
        print("Scale factor is {}".format(scale_factor))
        print("Warning: This scale factor is quite large so you\n"
              "might have issues with mixing bowl volumes and oven space.\n"
              "Please consider using a smaller scale factor and making more than one batch.")
        change_scale_factor = input("Press <Enter> to keep it, or <any other "
                                    "key> + <Enter> to change ")
        if not change_scale_factor:
            keep_scale_factor = True
    else:
        keep_scale_factor = True

print("Scale factor is {}".format(scale_factor))
