from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from recipes_api.models import RecipeModel
from recipes_api.serializers import RecipeSerializer


class RecipeListCreate(APIView):
    def get(self, request):
        recipes = RecipeModel.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


