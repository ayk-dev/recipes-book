from django.urls import path
from recipes_api import views

urlpatterns = [
    path('', views.RecipeListCreate.as_view(), name='list recipes'),
    path('<int:pk>', views.RecipeGetUpdateDelete.as_view(), name='recipe details'),
    path('<int:pk>/comments', views.CommentListCreate.as_view(), name='recipe comments'),

]
