from django.apps import AppConfig


class PretixControlConfig(AppConfig):
    name = 'pretix.control'
    label = 'pretixcontrol'

    def ready(self):
        from .views import dashboards
        from . import logdisplay
