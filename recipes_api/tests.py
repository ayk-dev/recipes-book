from django.contrib.auth import get_user_model
from django.test import TestCase
from recipes_api.models import RecipeModel, Comment

UserModel = get_user_model()

class Test_Create_Recipe(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = UserModel.objects.create_user(
            email='a@abv.bg', user_name='test_user1', first_name='aa', password='111')
        testuser1.save()

        test_recipe = RecipeModel.objects.create(
            category='breakfast',
            title='Recipe Title',
            description='Recipe Description',
            ingredients='Recipe Ingredients',
            time=10,
            servings=1,
            author_id=1,
        )
        test_recipe.save()

    def test_recipe_content(self):
        recipe = RecipeModel.objects.get(id=1)
        category = f'{recipe.category}'
        title = f'{recipe.title}'
        description = f'{recipe.description}'
        time = f'{recipe.time}'
        servings = f'{recipe.servings}'
        author = f'{recipe.author}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(category, 'breakfast')
        self.assertEqual(title, 'Recipe Title')
        self.assertEqual(description, 'Recipe Description')
        self.assertEqual(time, '10')
        self.assertEqual(servings, '1')
        self.assertEqual(author, 'test_user1')
        self.assertEqual(str(recipe), 'Recipe Title')


class Test_Comment_Recipe(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = UserModel.objects.create_user(
            email='a@abv.bg', user_name='test_user1', first_name='aa', password='111')
        testuser1.save()

        test_recipe = RecipeModel.objects.create(
            category='breakfast',
            title='Recipe Title',
            description='Recipe Description',
            ingredients='Recipe Ingredients',
            time=10,
            servings=1,
            author_id=1,
        )
        test_recipe.save()

        test_comment = Comment.objects.create(
            title='Test title',
            content='Test content comment',
            recipe_id=1,
        )
        test_comment.save()

    def test_comment_recipe(self):
        comment = Comment.objects.get(id=1)
        title = f'{comment.title}'
        content = f'{comment.content}'
        recipe = f'{comment.recipe}'
        self.assertEqual(title, 'Test title')
        self.assertEqual(recipe, 'Recipe Title')
        self.assertEqual(content, 'Test content comment')
        self.assertEqual(str(comment), 'Test title')




