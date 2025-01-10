from django.apps import AppConfig


class MoneysiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'moneysite'

class moneysite(AppConfig):  
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'moneysite' 

    def ready(self):
        import moneysite.signals 
