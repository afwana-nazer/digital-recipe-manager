from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/new/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_create'),
    path('recipe/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('recipe/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    
    path('register/', views.RegisterView.as_view(), name='register'),
]
