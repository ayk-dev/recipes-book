from rest_framework import serializers

from recipes_api.models import RecipeModel, IngredientsModel


class IngredientsSerializer(serializers.ModelSerializer):
    def validate(self, data):
        self.validate_type(data["quantity_type"])
        return data

    def validate_type(self, type):
        VALID_QUANTITY_TYPES = ['gr', 'grams', 'oz', 'tbsp', 'tsp', 'cup']
        if type.lower().rstrip('.') not in VALID_QUANTITY_TYPES:
            raise serializers.ValidationError("Quantity type must be one of the following grams/gr, oz, tbsp, tsp, cup")
        return type

    class Meta:
        model = IngredientsModel
        fields = ['name',]


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True)

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