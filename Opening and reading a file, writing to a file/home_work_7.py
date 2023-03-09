# Воспроизведите код с лекции 1.5 и дополните его следующим образом:

# Список рецептов должен храниться в отдельном файле в следующем формате:
#       Название блюда
#       Kоличество ингредиентов
#       Название ингредиента | Количество | Единица измерения
# Пример:
#       Омлетт
#       3
#       Яйца | 2 | шт
#       Молоко | 50 | г
#       Помидор | 100 | мл
# В одном файле может быть произвольное количество блюд.
# Читать список рецептов из этого файла.
# Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.
# Код выглядел следующим образом:

#     cook_book = {  
#       'яйчница': [
#         {'ingredient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#         {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#         ],
#       'стейк': [
#         {'ingredient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#         {'ingredient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#         {'ingredient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#         ],
#       'салат': [
#         {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#         {'ingredient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#         {'ingredient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#         {'ingredient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#         ]
#       }


#     def get_shop_list_by_dishes(dishes, person_count):
#       shop_list = {}
#       for dish in dishes:
#         for ingredient in cook_book[dish]:
#           new_shop_list_item = dict(ingredient)

#           new_shop_list_item['quantity'] *= person_count
#           if new_shop_list_item['ingredient_name'] not in shop_list:
#             shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
#           else:
#             shop_list[new_shop_list_item['ingredient_name']]['quantity'] +=
#               new_shop_list_item['quantity']
#       return shop_list

#     def print_shop_list(shop_list):
#       for shop_list_item in shop_list.values():
#         print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], 
#                                 shop_list_item['measure']))

#     def create_shop_list():
#       person_count = int(input('Введите количество человек: '))
#       dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
#         .lower().split(', ')
#       shop_list = get_shop_list_by_dishes(dishes, person_count)
#       print_shop_list(shop_list)

#     create_shop_list()

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
    with open('cooking_book.txt', encoding="utf-8") as file_to_read:
        while True:
            recipe_name = file_to_read.readline().strip()
            if recipe_name.strip() == '':
                break
            number_of_ingredients = int(file_to_read.readline().strip())
            list_of_ingredients = []
            for i in range(number_of_ingredients):
                ingredient = file_to_read.readline().strip().split(' | ')
                ingredients = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
                list_of_ingredients.append(ingredients)
            cook_book.update({recipe_name: list_of_ingredients})

def main():
    get_cooking_book()
    create_shop_list()
# test commit
main()
