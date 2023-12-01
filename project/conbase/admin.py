from django.apps import AppConfig


class StackbaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'conbase'

    def ready (self):
        import users.signals