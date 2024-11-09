from django.db import models


class Ingredient(models.Model):
    name = models.CharField("Название", max_length=255)
    unit = models.CharField("Единица измерения", max_length=50)
    stock_quantity = models.DecimalField("Количество на складе", max_digits=10, decimal_places=2)
    price_per_unit = models.DecimalField("Цена за единицу ингредиента", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", blank=True, null=True)
    instructions = models.TextField("Инструкция", blank=True, null=True)
    price_per_unit = models.DecimalField("Цена за единицу напитка", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class IngredientInDrink(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, verbose_name="Напиток")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name="Ингредиент")
    quantity = models.IntegerField("Количество")

    def __str__(self):
        return f"{self.ingredient.name} in {self.drink.name}"


class Order(models.Model):
    date = models.DateTimeField("Дата")
    cost = models.DecimalField("Стоимость", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.date}"


class DrinkInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, verbose_name="Напиток")
    quantity = models.IntegerField("Количество")

    def __str__(self):
        return f"{self.drink.name} in order {self.order.id}"
