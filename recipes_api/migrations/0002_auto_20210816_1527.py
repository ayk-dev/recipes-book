# Generated by Django 3.2.6 on 2021-08-16 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('breakfast', 'Breakfast'), ('appetizer', 'Appetizer'), ('main_course', 'Main course'), ('dessert', 'Dessert'), ('snack', 'Snack'), ('drink', 'Drink')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='recipemodel',
            options={'ordering': ['-updated']},
        ),
        migrations.RemoveField(
            model_name='recipemodel',
            name='method',
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users_auth.recipeuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='image',
            field=models.ImageField(default='recipes/default.png', upload_to='recipes'),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='ingredients',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='IngredientsModel',
        ),
        migrations.AddField(
            model_name='like',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes_api.recipemodel'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', related_query_name='like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='recipes_api.recipemodel'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
