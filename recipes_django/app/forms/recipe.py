from django import forms

from recipes_django.app.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        #exclude = ('profile',)