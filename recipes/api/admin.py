from django.contrib import admin
from .models import Recipe, Ingredient  # Import your models here

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'prep_time')  # Customize as needed

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'recipe')  # Customize as needed
