from django.apps import AppConfig


class PretixBaseConfig(AppConfig):
    name = 'pretix.base'
    label = 'pretixbase'

    def ready(self):
        from . import exporter  # NOQA
        from . import payment  # NOQA
        from . import exporters  # NOQA
        from . import invoice  # NOQA
        from . import notifications  # NOQA
        from . import email  # NOQA
        from .services import auth, checkin, export, mail, tickets, cart, orderimport, orders, invoices, cleanup, update_check, quotas, notifications, vouchers  # NOQA
        from django.conf import settings

        try:
            from .celery_app import app as celery_app  # NOQA
        except ImportError:
            pass

        if hasattr(settings, 'RAVEN_CONFIG'):
            from ..sentry import initialize
            initialize()


try:
    import pretix.celery_app as celery  # NOQA
except ImportError:
    pass
