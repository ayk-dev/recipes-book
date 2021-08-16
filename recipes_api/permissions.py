from rest_framework import permissions


class RecipeEditPermission(permissions.BasePermission):
    message = 'Editing recipe is restricted to author only'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        return obj.author == request.user

