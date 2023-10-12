from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    ingredients = models.CharField(max_length=80, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    time = models.IntegerField(
        null=True,
        blank=False,
        validators=[MaxValueValidator(60), MinValueValidator(0)],
    )

    def __str__(self):
        return self.name


class Rating(models.Model):
    recipe = models.ForeignKey(
        Recipe, blank=False, null=False, on_delete=models.CASCADE, unique=True
    )
    stars = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        validators=[MaxValueValidator(5), MinValueValidator(1)],
    )

    def __str__(self):
        return str(self.stars)
