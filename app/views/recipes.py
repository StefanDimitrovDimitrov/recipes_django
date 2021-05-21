from django.shortcuts import render


def create_recipe (request):
    return render(request, 'create.html')

def details_recipe(request):
    return render(request, 'details.html')

def edit_recipe(request):
    return render(request, 'edit.html')

def delete_recipe(request):
    return render(request, 'delete.html')
