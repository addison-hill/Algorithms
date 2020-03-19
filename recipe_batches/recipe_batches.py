#!/usr/bin/python

import math

# My first pass solution didnt pass all tests, needed fixing on total batches

# def recipe_batches(recipe, ingredients):
#     total_batches = 0

#     for i in recipe:
#         if ingredients.get(i) == None:
#             return 0
#         print(i)
#         print(ingredients[i])
#         if recipe[i] <= ingredients[i]:
#             # total_batches += 1
#             ingredients[i] = ingredients[i] - recipe[i]
#             print("new ingredients", ingredients[i])
#         else:
#             return total_batches

#     return total_batches

# Solution from after hours


def recipe_batches(recipe, ingredients):
    max_batches = float('inf') # <---- set infinity so that max_batches is always greater than ingredients[key] on line 32 to start with
    for key, value in recipe.items():
        if key not in ingredients: # <---- edge case for if we dont have the ingredient needed in the recipe
            return 0
        if max_batches > ingredients[key] // value:  # the floor division // rounds the result down to the nearest whole number
            max_batches = ingredients[key] // value  # this will get overrided if any other max_batches for a certain key is less

    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
