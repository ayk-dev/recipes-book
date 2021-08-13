from django.db import models
from django.contrib.auth.models import User


# TODO UserModel = get_user_model() insted of User
from django.utils import timezone


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

    title = models.CharField(max_length=50)

    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
    )

    ingredients = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
    )

    time = models.PositiveIntegerField()

    servings = models.PositiveIntegerField()

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    image = models.ImageField(
        upload_to='recipes',
        default='recipes/default.png',
    )

    # author = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    # )
    class Meta:
        ordering = ['updated']

    def __str__(self):
        return self.title


class Like(models.Model):
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes',
        related_query_name='like',
    )


class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    recipe = models.ForeignKey(
        RecipeModel,
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comment',
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title