from django.shortcuts import render, redirect

from recipes_django.app.forms.recipe import RecipeForm
from recipes_django.app.models import Recipe


def create_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)
    else:
        recipe = Recipe()
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'create.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    name = recipe.title
    ingredients = recipe.ingredients.split(',')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
        'name': name
    }
    return render(request, 'details.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': RecipeForm(instance=recipe),
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'recipe': recipe,
            'form': form,
        }

        return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    return render(request, 'delete.html')
