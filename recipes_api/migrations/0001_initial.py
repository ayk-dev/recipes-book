# Generated by Django 3.2.6 on 2021-08-07 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('breakfast', 'Breakfast'), ('appetizer', 'Appetizer'), ('main_course', 'Main course'), ('dessert', 'Dessert'), ('snack', 'Snack'), ('drink', 'Drink')], max_length=12)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('method', models.TextField(max_length=1000)),
                ('time', models.PositiveIntegerField()),
                ('servings', models.PositiveIntegerField()),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes_api.ingredientsmodel')),
            ],
        ),
    ]
