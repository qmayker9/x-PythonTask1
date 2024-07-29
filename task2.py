def fix_ingredients(ingredients: list) -> list:
    fixed_ingredients = []

    for ingredient in ingredients:
        if ingredient.lower()[0] != 'z':

            fixed_ingredients.append(ingredient[::-1])
        else:
            fixed_ingredients.append(ingredient)

    return fixed_ingredients


