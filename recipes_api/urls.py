from django.urls import path
from recipes_api import views

urlpatterns = [
    path('', views.RecipeListCreate.as_view()),
    path('<int:pk>', views.RecipeGetUpdateDelete.as_view()),
    path('<int:pk>/comments', views.CommentListCreate.as_view()),

]
