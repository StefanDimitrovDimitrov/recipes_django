from django.shortcuts import render

from app.models import Recipe


def create_recipe (request):
    return render(request, 'create.html')

def details_recipe(request, pk):
    recipe = Recipe.objects.all(pk=pk)
    context = {
        'recipe': recipe
    }
    return render(request, 'details.html', context)

def edit_recipe(request, pk):
    return render(request, 'edit.html')

def delete_recipe(request, pk):
    return render(request, 'delete.html')
