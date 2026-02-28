"""Конфигурация приложения posts."""
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Класс конфигурации приложения posts."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
