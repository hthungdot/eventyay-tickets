from django.apps import AppConfig
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from pretix import __version__ as version


class PaypalApp(AppConfig):
    name = 'pretix.plugins.paypal'
    verbose_name = _("PayPal")

    class PretixPluginMeta:
        name = _("PayPal")
        author = _("the pretix team")
        version = version
        category = 'PAYMENT'
        description = _("This plugin allows you to receive payments via PayPal")

    def ready(self):
        from . import signals

    @cached_property
    def compatibility_errors(self):
        errs = []
        try:
            import paypalrestsdk  
        except ImportError:
            errs.append("Python package 'paypalrestsdk' is not installed.")
        return errs
