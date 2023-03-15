from django.shortcuts import render, redirect

from .forms import RecipeForm

from .models import Recipe


def index(request):
    recipes = Recipe.objects.order_by('-post_date')
    recipes_count = Recipe.objects.count()
    users_count = Recipe.objects.values('creator').distinct().count()
    context = {'recipes': recipes, 'recipes_count': recipes_count, 'users_count': users_count}
    return render(request, 'recipes/index.html', context)


def new_recipe(request):
    # GET request for rendering the page.
    if request.method != 'POST':
        form = RecipeForm()
    # POST request for adding a new recipe.
    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes:index')

    context = {'form': form}
    return render(request, 'recipes/new_recipe.html', context)


def recipe_page(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_page.html', context)


def my_recipes(request):
    recipes = Recipe.objects.filter(creator=request.user.username).order_by('-post_date')
    context = {'recipes': recipes}
    return render(request, 'recipes/my_recipes.html', context)


def search(request):
    if request.GET['recipe_search']:
        recipe_title = request.GET['recipe_search']
        recipes = Recipe.objects.filter(title__contains=recipe_title)
        if not recipes:
            return redirect('recipes:not_found')
        else:
            recipe_id = recipes[0].id
            return redirect('recipes:recipe_page', recipe_id)


def not_found(request):
    return render(request, 'recipes/recipe_not_found.html')


def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
    else:
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:index')
    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipes/edit_recipe.html', context)


def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.delete()
    return redirect('recipes:my_recipes')
