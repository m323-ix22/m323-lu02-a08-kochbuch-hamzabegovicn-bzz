import json

"""
Pure Function zum Laden des Rezepts von JSON zu Python-Dictionary
"""


def load_recipe(recipe_json: str) -> dict:
    return json.loads(recipe_json)


def adjust_recipe(recipe: dict, num_persons: int) -> dict:
    factor = num_persons / recipe['servings']

    new_ingredients = {ingredient: amount * factor for ingredient, amount in recipe['ingredients'].items()}

    return {
        "title": recipe["title"],
        "ingredients": new_ingredients,
        "servings": num_persons
    }


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')

    num_persons = 2

    recipe = load_recipe(recipe_json)

    adjusted_recipe = adjust_recipe(recipe, num_persons)

    print(json.dumps(adjusted_recipe, indent=4))
