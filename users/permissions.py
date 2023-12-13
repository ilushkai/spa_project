from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Возможность доступа только пользователю"""

    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.user.pk:
            return True
        else:
            return False