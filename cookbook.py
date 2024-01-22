with open("recipes.txt", encoding="utf-8") as cook_file:
    cook_book = {}
    for line in cook_file:
        dish = line.strip()
        ingredients_count = int(cook_file.readline().strip())
        ingredients = []
        for _ in range(ingredients_count):
            ingredient_name, quantity, measure = cook_file.readline().strip().split(" | ")
            ingredients.append({
                "ingredient_name": ingredient_name,
                "quantity": quantity,
                "measure": measure
            })
        cook_book[dish] = ingredients
        cook_file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    list_of_dishes = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            ingredients_count = dict([(ingredients['ingredient_name'],
                                     {'quantity': int(ingredients['quantity']) * person_count,
                                      'measure': ingredients['measure']})])
            if list_of_dishes.get(ingredients['ingredient_name']) == 'None':
                _merger = (int(list_of_dishes[ingredients['ingredient_name']]['quantity']) +
                           int(ingredients_count[ingredients['ingredient_name']]['quantity']))
                list_of_dishes[ingredients['ingredient_name']]['quantity'] = _merger
            else:
                list_of_dishes.update(ingredients_count)    
    return list_of_dishes
print(get_shop_list_by_dishes(['Омлет'], 2))
            
            
        
            

