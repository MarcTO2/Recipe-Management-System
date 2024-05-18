from django.db import models

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    ingredients = models.TextField()
    cooking_instructions = models.TextField()
    difficulty = models.CharField(
        max_length=6,
        choices=DIFFICULTY_CHOICES,
        default=DIFFICULTY_CHOICES[1][0],
    )

    def __str__(self):
        return self.title