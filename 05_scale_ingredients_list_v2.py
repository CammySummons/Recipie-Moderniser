"""Evaluates fractions for scale factor, rounds scaled amounts, and
prevents entry of digits in ingredient name
Created by Sammy Cummins
Version 2
17/06/2021
"""


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


# Ask user for ingredient name
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if not response:  # checks if response has been entered
            print("Please enter an ingredient name (cannot be blank)")  # and
            # if not generates the error message above

        elif not response.isalpha():  # checks to ensure the ingredient name
            # contains no digits
            print("The ingredient name can't contain digits.")

        else:  # where no error found
            return response


# Main Routine

# Replace line below with component 3 (number checking function) in due course
scale_factor = eval(input("Scale Factor: "))  # eval allows the scale factor
# to be entered as fraction eg 1/3
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

            # Remove decimal point for whole numbers
            if scaled % 1 == 0:
                scaled = int(scaled)
            elif scaled * 10 % 1 == 0:
                scaled = "{:.1f}".format(scaled)  # 1dp (removes 2nd dp if it is 0 eg .50)
            else:
                scaled = "{:.2f}".format(scaled)  # 2dp

            ingredient_name = not_blank("Enter ingredient name : ").title()
            # Calls the not_blank function and provides the question
            ingredient_list.append("{} units {}".format(scaled, ingredient_name))
            # Puts both elements on the same line

    elif len(ingredient_list) > 1:
        valid_list = True
        # If list contains at least two items break out of loop
        print("Here are your ingredients:")
        for item in ingredient_list:
            print(item)  # Output list
    else:
        print("Please enter at least two ingredients")
