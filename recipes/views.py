from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Recipe, Category
from .forms import RecipeForm, CategoryForm
from django.db.models import Q

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('recipes:recipe_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('recipes:recipe_list')

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = Recipe.objects.select_related('author', 'category').all().order_by('-created_at')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('category')
        
        if q:
            queryset = queryset.filter(title__icontains=q)
        if cat:
            queryset = queryset.filter(category__name__iexact=cat)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes:dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    form_class = RecipeForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def get_success_url(self):
        return reverse('recipes:recipe_detail', kwargs={'pk': self.object.pk})

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipes:dashboard')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'recipes/category_form.html'
    form_class = CategoryForm
    
    def get_success_url(self):
        return reverse('recipes:recipe_create')

class DashboardView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/dashboard.html'
    context_object_name = 'my_recipes'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorite_recipes'] = self.request.user.favorited_recipes.all().order_by('-created_at')
        return context

def toggle_favorite(request, pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (reverse('login'), request.path))
    
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
        messages.success(request, f'Removed {recipe.title} from favorites.')
    else:
        recipe.favorites.add(request.user)
        messages.success(request, f'Added {recipe.title} to favorites.')
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('recipes:recipe_detail', args=[pk])))
