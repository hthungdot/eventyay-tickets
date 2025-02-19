from django.apps import AppConfig
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from pretix import __version__ as version


class ReportsApp(AppConfig):
    name = 'pretix.plugins.reports'
    verbose_name = _("Report exporter")

    class PretixPluginMeta:
        name = _("Report exporter")
        author = _("the pretix team")
        version = version
        category = 'FORMAT'
        description = _("This plugin allows you to generate printable reports about your sales.")

    def ready(self):
        from . import signals 

    @cached_property
    def compatibility_errors(self):
        errs = []
        try:
            import reportlab
        except ImportError:
            errs.append("Python package 'reportlab' is not installed.")
        return errs
