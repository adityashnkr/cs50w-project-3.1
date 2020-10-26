from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    PIZZA = "Pizza"
    PASTA = "Pasta"
    CATEGORY_CHOICES = (
        (PIZZA, "Pizza"),
        (PASTA, "Pasta")
    )

    name = models.CharField(max_length=16, choices=CATEGORY_CHOICES)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    S = 'Small'
    L = 'Large'
    SIZE_CHOICES = (
        (S, 'Small'),
        (L, 'Large')
    )
    size = models.CharField(max_length=5, choices=SIZE_CHOICES)
    price = models.IntegerField(default=0, blank=True)


class Pizza(Item):
    REGULAR = "Regular"
    SICILAIN = "Sicilian"
    CRUST_CHOICES = {
        (REGULAR, "Regular"),
        (SICILAIN, "Sicilain")
    }
    crust = models.CharField(max_length=8, choices=CRUST_CHOICES, null=True)
    max_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.crust} Pizza with {self.name} ({self.size}) _ {self.price}"


class Topping(Item):
    """Define toppings."""

    def __str__(self):
        return f"{self.name}"


class Sub(Item):
    """Define sub-menus."""

    def __str__(self):
        return f"{self.name} ({self.size}) _ {self.price}"


class Extra(Item):
    """Define extra-options."""

    def __str__(self):
        return f"{self.name}"


class Pasta(Item):
    """Define pastas."""

    def __str__(self):
        return f"{self.name} _ {self.price}"


class Salad(Item):
    """Define salads."""

    def __str__(self):
        return f"{self.name} _ {self.price}"


class Dinner(Item):
    """Define dinner platters."""

    class Meta:
        verbose_name = "Dinner Platter"
        verbose_name_plural = "Dinner Platters"

    def __str__(self):
        return f"{self.name} ({self.size}) _ {self.price}"
