from django.db import models


class IngredientsModel(models.Model):
    name = models.CharField(
        max_length=50,
    )
    quantity = models.CharField(
        max_length=50,
    )


class RecipeModel(models.Model):
    TYPE_CHOICE_BREAKFAST = 'breakfast'
    TYPE_CHOICE_APPETIZER = 'appetizer'
    TYPE_CHOICE_MAINCOURSE = 'main_course'
    TYPE_CHOICE_DESSERT = 'dessert'
    TYPE_CHOICE_SNACK = 'snack'
    TYPE_CHOICE_DRINK = 'drink'

    TYPE_CHOICES = (
        (TYPE_CHOICE_BREAKFAST, 'Breakfast'),
        (TYPE_CHOICE_APPETIZER, 'Appetizer'),
        (TYPE_CHOICE_MAINCOURSE, 'Main course'),
        (TYPE_CHOICE_DESSERT, 'Dessert'),
        (TYPE_CHOICE_SNACK, 'Snack'),
        (TYPE_CHOICE_DRINK, 'Drink')
    )

    category = models.CharField(
        max_length=12,
        choices=TYPE_CHOICES,
        # null=True,
        # blank=True,
    )

    title = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
    )

    ingredients = models.ManyToManyField(IngredientsModel, related_name='ingredients')

    method = models.TextField(
        max_length=1000,
    )

    time = models.PositiveIntegerField()

    servings = models.PositiveIntegerField()

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    # image = models.ImageField(
    #     upload_to='pets',
    # )

    # author = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE,
    # )




