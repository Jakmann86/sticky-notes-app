from django.apps import AppConfig

# Configuration class for the 'sticky_app' Django application
class StickyAppConfig(AppConfig):
    # Specify the default auto field type for models
    default_auto_field = 'django.db.models.BigAutoField'
    # Specify the name of the Django application
    name = 'sticky_app'
