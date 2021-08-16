from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from recipes_api.models import RecipeModel
from recipes_api.serializers import RecipeSerializer
from recipes_api.permissions import RecipeEditPermission
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class RecipeListCreate(generics.ListCreateAPIView):
    # def get(self, request):
    #     recipes = RecipeModel.objects.all()
    #     serializer = RecipeSerializer(recipes, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = RecipeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeSerializer


class RecipeGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView, RecipeEditPermission):
    # def put(self, request, recipe_id):
    #     recipe = get_object_or_404(RecipeModel, pk=recipe_id)
    #     serializer = RecipeSerializer(recipe, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    #
    # def get(self, request, recipe_id):
    #     try:
    #         recipe = RecipeModel.objects.get(id=recipe_id)
    #         recipe_serializer = RecipeSerializer(recipe)
    #         return Response(recipe_serializer.data)
    #     except:
    #         return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    #
    # def delete(self, request, recipe_id):
    #     try:
    #         recipe = RecipeModel.objects.get(id=recipe_id)
    #         recipe.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     except Exception as ex:
    #         return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    permission_classes = [RecipeEditPermission]

    queryset = RecipeModel.objects.all()
    serializer_class = RecipeSerializer
