"""Takes external csv and converts amount from mls to gms
Created by Sammy Cummins
Version 2
20/06/2020
"""

import csv

# open file using appropriately named variable
groceries = open('01_ingredients_ml_to_g.csv')

# Read data from above into a list
csv_groceries = csv.reader(groceries)

# Create a dictionary to hold the data
food_dictionary = {}

# Add the data from the list into the dictionary
# (first item in row is key, and next is definition)
for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

complete_list = False
while not complete_list:
    amount = eval(input("How much?: "))

    # Get ingredient and change it to match dictionary
    ingredient = input("Ingredient: ").lower()

    if ingredient in food_dictionary:
        factor = food_dictionary.get(ingredient)
        amount = amount * float(factor) / 250
        print("amount in g {}".format(amount))
    else:
        print("{} is unchanged".format(amount))


