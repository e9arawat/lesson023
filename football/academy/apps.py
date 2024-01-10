"""
    Module name :- apps
"""

from django.apps import AppConfig


class AcademyConfig(AppConfig):
    """
    Path of an app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "academy"
