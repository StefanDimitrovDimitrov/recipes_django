from django.urls import path

from app.views.index import index
from app.views.recipes import create_recipe, edit_recipe, delete_recipe, details_recipe

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_recipe, name='create'),
    path('edit/<int:pk>', edit_recipe, name='edit'),
    path('delete/<int:pk>', delete_recipe, name='delete'),
    path('details/', details_recipe, name='details'),
]