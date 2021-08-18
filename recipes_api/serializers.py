from rest_framework import serializers

from recipes_api.models import RecipeModel, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['title', 'content', 'user', 'created']


class RecipeSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = RecipeModel
        fields = '__all__'





