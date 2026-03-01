from django.apps import AppConfig

class User3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user3'

    def ready(self):
        import user3.signals