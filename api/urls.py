from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = "api"
urlpatterns = [
    path("", views.RecipeList, name="recipe"),
    path("<int:recipe_id>/edit-recipe/", views.RecipeEdit, name="edit-recipe"),
    path("<int:recipe_id>/delete-recipe/", views.RecipeDelete, name="delete-recipe"),
    path("login/", views.LoginView, name="login"),
    path("register/", views.registerView, name="register"),
    path("logout/", views.LogoutView, name="logout"),
    path("<int:recipe_id>/rating/", views.RateView, name="rate-recipe"),
]
