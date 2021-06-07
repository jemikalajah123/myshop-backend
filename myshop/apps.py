from django.apps import AppConfig


class MyshopConfig(AppConfig):
    name = 'myshop'

    def ready(self):
        import myshop.signals
