#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    total_batches = 0
    if len(recipe) == len(ingredients):
        for i in recipe:
            print(ingredients[i])
            if recipe[i] <= ingredients[i]:
                total_batches += 1
                ingredients[i] = ingredients[i] - recipe[i]
                print(ingredients[i])

    return total_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
