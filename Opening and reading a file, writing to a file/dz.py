from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in dishes[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
    else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
        new_shop_list_item['quantity']
    return shop_list
def get_cook_book_with_quantity():
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

print(get_cook_book_with_quantity())
print(get_shop_list_by_dishes('Омлет', 2))



