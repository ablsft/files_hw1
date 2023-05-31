import os

def path_to_file(file_name):
    current_folder = os.getcwd()
    return os.path.join(current_folder, file_name)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in cook_book:
        if dish in dishes:
            for ingred in cook_book[dish]:
                if ingred['ingredient_name'] in shop_list:
                    shop_list[ingred['ingredient_name']]['quantity'] += ingred['quantity'] * person_count
                else:
                    shop_list[ingred['ingredient_name']] = {'measure': ingred['measure'], 'quantity': ingred['quantity'] * person_count}
    
    return shop_list

with open(path_to_file('recipes.txt'), encoding='utf-8') as recipes:
    cook_book = {}
    for dish in recipes:
        ingred_quantity = int(recipes.readline())
        ingred_list = []
        for i in range(ingred_quantity):
            ingredient_name, quantity, measure = recipes.readline().split(' | ')
            ingred_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()})
        recipes.readline()
        cook_book[dish.strip()] = ingred_list
        
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))
