from rest_framework import serializers

from recipes_api.models import RecipeModel


class RecipeSerializer(serializers.ModelSerializer):
   
    def validate(self, data):
        self.validate_title(data["title"])
        return data

    def validate_title(self, title):
        if title:
            if not title[0].isupper():
                raise serializers.ValidationError("Title must start with capital")
        return title

    class Meta:
        model = RecipeModel
        fields = '__all__'
