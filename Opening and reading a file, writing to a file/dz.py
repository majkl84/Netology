from pprint import pprint
cook_book = {}
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
    person_count = int(input('Введите нужное количество человек: '))
    dishes = input('Введите требуемые блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

def get_cooking_book():
    with open("recipes.txt",encoding="utf-8") as file_with_food:
        while True:
            recipe_name = file_with_food.readline().strip()
            if recipe_name.strip() == '':
                break
            number_of_ingredients = int(file_with_food.readline().strip())
            list_of_ingredients = []
            for i in range(number_of_ingredients):
                ingredient = file_with_food.readline().strip().split(' | ')
                ingredients = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
                list_of_ingredients.append(ingredients)
            cook_book.update({recipe_name: list_of_ingredients})


def main():
    get_cooking_book()
    create_shop_list()

