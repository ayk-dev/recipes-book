from django.contrib import admin

from recipes_api.models import RecipeModel, IngredientsModel


@admin.register(RecipeModel)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['category', 'title']
    sortable_by = ('title', 'category')
    list_filter = ('category', 'title')

    def likes_count(self, obj):
        return obj.likes.count()



