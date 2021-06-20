"""Get the scale factor, then the ingredient and amount required for each
then add the ingredients with their scaled amounts into a list to be printed
at the end.
Created by Sammy Cummins
Version 1
16/06/2021
"""


# Ask user for ingredient name
def not_blank(response):
    error = "Please enter an ingredient name (cannot be blank)"
    valid = False

    while not valid:
        response = input(response)

        if not response:  # checks if response has been entered
            print(error)  # and if not generates the error message

        else:  # where no error found
            return response


# Number checking function
def num_check(response):
    error = "You must enter a number more than 0"
    valid = False
    while not valid:
        try:
            if response <= 0:
                response = float(input("Please enter a number more than 0: "))
            else:
                return response
        except ValueError:
            print(error)


# Main Routine

# Replace line below with component 3 (number checking function) in due course
scale_factor = float(input("Scale Factor: "))
ingredient_list = []  # Set up ingredient list
valid_list = False

while not valid_list:

    amount = input("Enter amount (or 'X' to exit): ")
    if amount.upper() != "X":
        if not amount or not amount.isdigit():  # Won't allow blank or strings
            print("Please enter a valid amount")
        else:
            amount = float(amount)  # Converts amount to a float
            scaled = num_check(amount) * scale_factor
            ingredient_name = not_blank("Enter ingredient name: ").title()
            # Calls the not_blank function and provides the question
            ingredient_list.append("{} units {}".format(scaled, ingredient_name))
            # Puts both elements on the same line

    elif len(ingredient_list) > 1:
        valid_list = True
        # If list contains at least two items break out of loop
        print("Here are your ingredients: ")
        for item in ingredient_list:
            print(item)  # Output list

    else:
        print("Please enter at least two ingredients")
