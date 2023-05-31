import os

def path_to_file(file_name):
    current_folder = os.getcwd()
    return os.path.join(current_folder, file_name)

with open(path_to_file('recipes.txt'), encoding='utf-8') as recipes:
    cook_book = {}
    for dish in recipes:
        ingred_quantity = int(recipes.readline())
        ingred_list = []
        for i in range(ingred_quantity):
            ingredient_name, quantity, measure  = recipes.readline().split(' | ')
            ingred_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()})
        recipes.readline()
        cook_book[dish.strip()] = ingred_list
    
print(cook_book)