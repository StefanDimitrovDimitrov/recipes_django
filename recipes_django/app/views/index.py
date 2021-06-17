from django.shortcuts import render

from recipes_django.app.models import Recipe

def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html',context)
