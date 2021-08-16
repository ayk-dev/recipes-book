from django.contrib import admin

from recipes_api.models import RecipeModel, Comment

admin.site.site_header = 'Cooking monster admin'


@admin.register(RecipeModel)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['category', 'title']
    sortable_by = ('title', 'category')
    list_filter = ('category', 'title')

    def likes_count(self, obj):
        return obj.likes.count()




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


