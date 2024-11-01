from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
    'kofe': {
        'растворимый кофе, г': 10,
        'вода, л': 0.3,
    },
}

def get_recipe(request, dish):
    servings = int(request.GET.get("servings", 1))
    recipe = dict(DATA.get(dish))
    #Словарь-рецепт recipe останется пустым, если блюдо неизвестно
    if recipe:
        for ingredient, amount in recipe.items():
            recipe[ingredient] = amount * servings
    context = { 'recipe': recipe }
    return render(request, 'calculator/index.html', context)