from django import forms
from .models import Recipe, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-brand-cinnabar focus:ring-brand-cinnabar py-2 px-3 border',
                'placeholder': 'E.g. Breakfast, Vegan, Desserts...'
            })
        }

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'category', 'cook_time', 'image', 'ingredients', 'instructions']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-brand-cinnabar focus:ring-brand-cinnabar py-2 px-3 border',
            }),
            'category': forms.Select(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-brand-cinnabar focus:ring-brand-cinnabar py-2 px-3 border',
            }),
            'cook_time': forms.NumberInput(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-brand-cinnabar focus:ring-brand-cinnabar py-2 px-3 border', 
                'min': '0'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full text-gray-500 dark:text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-medium file:bg-brand-cream file:text-brand-cinnabar hover:file:bg-amber-100 cursor-pointer border border-gray-300 dark:border-gray-600 dark:bg-gray-700 rounded-md', 
                'accept': 'image/*'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-brand-cinnabar focus:ring-brand-cinnabar py-2 px-3 border placeholder-gray-400', 
                'rows': 2, 
                'placeholder': 'Briefly describe what makes this recipe special...'
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-brand-cinnabar focus:ring-brand-cinnabar py-2 px-3 border placeholder-gray-400', 
                'rows': 4, 
                'placeholder': '2 cups flour\n1 tsp baking powder\n...'
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-brand-cinnabar focus:ring-brand-cinnabar py-2 px-3 border placeholder-gray-400', 
                'rows': 6, 
                'placeholder': '1. Preheat oven to 350°F.\n2. Whisk together dry ingredients.\n...'
            }),
        }
