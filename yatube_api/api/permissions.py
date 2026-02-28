# api/permissions.py
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Если это безопасный метод (GET, HEAD, OPTIONS) - разрешаем
        if request.method in permissions.SAFE_METHODS:
            return True
        # В противном случае проверяем, что пользователь - автор
        return obj.author == request.user