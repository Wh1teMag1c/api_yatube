"""Модуль описания прав доступа для API."""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешение на изменение только для автора объекта."""

    def has_object_permission(self, request, view, obj):
        """Проверка прав на уровне отдельного объекта."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
