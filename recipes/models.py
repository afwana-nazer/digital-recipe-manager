from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    cook_time = models.PositiveIntegerField(help_text="Cook time in minutes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='recipes')
    favorites = models.ManyToManyField(User, related_name='favorited_recipes', blank=True)

    def __str__(self):
        return self.title
