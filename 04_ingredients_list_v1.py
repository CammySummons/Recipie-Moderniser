"""Get the ingredients required to make recipe, adding them to list
and then printing the list at the end
Created by Sammy Cummins
Version 1
16/06/2021
"""


# Ask user for ingredient name
def not_blank(question):
    error = "Please enter an ingredient name (cannot be blank)"
    valid = False

    while not valid:
        response = input(question)

        if not response:  # checks if response has been entered
            print(error)  # and if not generates the error message

        else:  # where no error found
            return response


# Main Routine
ingredient_list = []  # Set up ingredient list
valid_list = False
while not valid_list:
    ingredient_name = not_blank("Enter ingredient name (or 'X' to exit): ")\
        .title()  # Calls the not_blank function and provides the question
    if ingredient_name != "X":  # Check for escape code
        ingredient_list.append(ingredient_name)  # If exit code not entered,
        # add ingredient to list
    else:
        if len(ingredient_list) < 2:  # Check that list contains 2 items
            print("Please enter at least two ingredients")
        else:
            valid_list = True  # If list contains 2 items break out of loop
            print("Here are your ingredients:\n{}".format(ingredient_list))
