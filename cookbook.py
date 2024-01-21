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
print(cook_book)      