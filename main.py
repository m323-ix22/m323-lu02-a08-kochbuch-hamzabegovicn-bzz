"""
Funktionen  zum Bearbeiten eines JSON-basierten Kochbuchs.
"""
import json


def load_recipe(recipe_json: str) -> dict:
    return json.loads(recipe_json)


def adjust_recipe(recipe: dict, persons: int) -> dict:
    factor = persons / recipe["servings"]

    new_ingredients = {ingredient: amount * factor for ingredient, amount in recipe["ingredients"].items()}

    return {
        "title": recipe["title"],
        "ingredients": new_ingredients,
        "servings": persons
    }


if __name__ == "__main__":
    recipe_json_data = ("{\"title\": \"Spaghetti Bolognese\", \"ingredients\": {\"Spaghetti\": 400, \"Tomato Sauce\": "
                        "300, \"Minced Meat\": 500}, \"servings\": 4}")

    new_persons = 2

    loaded_recipe = load_recipe(recipe_json_data)

    updated_recipe = adjust_recipe(loaded_recipe, new_persons)

    print(json.dumps(updated_recipe, indent=4))
