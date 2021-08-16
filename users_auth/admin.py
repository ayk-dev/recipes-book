from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class RecipeUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'user_name', 'first_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('start_date',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('start_date',)
