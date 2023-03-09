from pprint import pprint
cook_book = {}

with open("recipes.txt",encoding="utf-8") as file_with_food:
    while True:
        name = file_with_food.readline().strip()
        if not name:
            break
        count = int(file_with_food.readline().strip())
        cook_book[name] = []
        line = file_with_food.readline().strip()
        while line:
            ingredients = line.split(" | ")
            ingredients_dict = {"ingredient_name": ingredients[0],
                                "quantity": int(ingredients[1]),
                                "measure": ingredients[2]}
            cook_book[name].append(ingredients_dict)
            line = file_with_food.readline().strip()
pprint(cook_book)



