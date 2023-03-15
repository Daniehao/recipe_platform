from django.db import models
from django.utils.timezone import now


class Recipe(models.Model):
    class DishType(models.TextChoices):
        AMERICAN = "American",
        INDIAN = "Indian",
        CHINESE = "Chinese",
        MEXICAN = "Mexican",
        FASTFOOD = "Fast Food",
        THAI = "Thai",
        KOREAN = "Korean",
        DESSERT = "Dessert"

    class Difficulty(models.TextChoices):
        EASY = "Easy",
        MEDIUM = "Medium",
        HARD = "Hard",

    title = models.CharField(max_length=50)
    creator = models.CharField(max_length=30)
    post_date = models.DateTimeField(default=now)
    dish_type = models.CharField(max_length=30, choices=DishType.choices, default=DishType.AMERICAN)
    difficulty = models.CharField(max_length=30, choices=Difficulty.choices, default=Difficulty.EASY)
    photo_1 = models.ImageField()
    photo_2 = models.ImageField(blank=True)
    recipe_content = models.CharField(max_length=500)

    def __str__(self):
        return self.title