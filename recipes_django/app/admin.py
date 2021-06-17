from django.contrib import admin

# Register your models here.
from recipes_django.app.models import Recipe

admin.site.register(Recipe)