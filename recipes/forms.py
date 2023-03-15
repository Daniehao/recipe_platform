from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['creator', 'title', 'post_date', 'dish_type', 'difficulty', 'photo_1', 'photo_2', 'recipe_content']
