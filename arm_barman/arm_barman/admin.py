from django.contrib import admin
from .models import Ingredient, Drink, IngredientInDrink, Order, DrinkInOrder

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Drink)
admin.site.register(IngredientInDrink)
admin.site.register(Order)
admin.site.register(DrinkInOrder)
