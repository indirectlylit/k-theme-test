from __future__ import absolute_import, print_function, unicode_literals
from django.views.generic.base import TemplateView


class UnWomenPluginView(TemplateView):
    template_name = "kolibri_un_women_plugin/kolibri_un_women_plugin.html"
