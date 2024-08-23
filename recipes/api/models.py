from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    prep_time = models.PositiveIntegerField()

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
