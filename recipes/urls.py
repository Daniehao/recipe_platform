from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('my_recipes/', views.my_recipes, name='my_recipes'),
    path('search/', views.search, name='search'),
    path('not_found/', views.not_found, name='not_found'),
    path('recipe_page/<recipe_id>/', views.recipe_page, name='recipe_page'),
    path('edit_recipe/<recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete_recipe/<recipe_id>/', views.delete_recipe, name='delete_recipe')
]
