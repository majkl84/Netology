# cook_book = {
#     'яйчница': [
#         {'ingredient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#         {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#     ],
#     'стейк': [
#         {'ingredient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#         {'ingredient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#         {'ingredient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#     'салат': [
#         {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#         {'ingredient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#         {'ingredient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#         {'ingredient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#     ]
# }
cook_book = {}

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

    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def get_cook_book_with_quantity(cook):

    with open(cook, encoding='utf-8') as f:
        while True:
            name = f.readline().strip()
            if not name:
                break
            count = int(f.readline().strip())
            cook_book[name] = []
            line = f.readline().strip()
            while line:
                ingredients = line.split(" | ")
                ingredients_dict = {"ingredient_name": ingredients[0],
                                    "quantity": int(ingredients[1]),
                                    "measure": ingredients[2]}
                cook_book[name].append(ingredients_dict)
                line = f.readline().strip()

    return cook_book


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    cook_book = get_cook_book_with_quantity("recipes.txt")
    shop_list = get_shop_list_by_dishes(cook_book, person_count)
    print_shop_list(shop_list)


create_shop_list()