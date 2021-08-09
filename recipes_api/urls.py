from django.urls import path
from recipes_api import views

urlpatterns = [
    path('', views.RecipeListCreate.as_view()),
    path('<int:recipe_id>', views.RecipeGetUpdateDelete.as_view()),

]