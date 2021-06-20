"""Get amount and unit from user then check if unit is in dictionary of units
If it is, convert to mls, otherwise leave as is
Created by Sammy Cummins
Version 2 - adds loop for testing purposes
20/06/2021
"""


# set up dictionary
unit_dict = {
    "tsp": 5,
    "tbsp": 15,
    "cup": 250,
    "ounce": 28.35,
    "pint":	473,
    "quart": 946,
    "pound": 454
}

complete_list = False
while not complete_list:
    # ask user for amount
    amount = eval(input("How much? "))

    # ask user for unit
    unit = input("Unit? ")

    # check if the unit is in the dictionary
    # if unit in dictionary, convert to ml
    # if no unit given or unit is unknown, leave as is
    if unit in unit_dict:
        factor = unit_dict.get(unit)
        amount *= factor
        print("amount in ml {}".format(amount))
    else:
        print("{} in unchanged".format(amount))

    # To end the loop of items to check
    another_item = input("\nPress <enter> to add another item \n"
                         "or any key + <enter> to end:\n")
    if not another_item:
        continue
    else:
        complete_list = True
