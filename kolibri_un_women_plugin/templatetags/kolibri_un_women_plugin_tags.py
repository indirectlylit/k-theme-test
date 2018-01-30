# coding=utf-8
"""
kolibri_un_women_plugin template tags
========================
Tags for including plugin javascript assets into a template.
"""

from __future__ import absolute_import, print_function, unicode_literals
from django import template
from kolibri.core.webpack.utils import webpack_asset_render
from .. import hooks

register = template.Library()


@register.simple_tag()
def kolibri_un_women_plugin_assets():
    """
    Using in a template will inject script tags that include the javascript assets defined
    by any concrete hook that subclasses UnWomenPluginSyncHook.
    :return: HTML of script tags to insert into kolibri_un_women_plugin/kolibri_un_women_plugin.html
    """
    return webpack_asset_render(hooks.UnWomenPluginSyncHook, async=False)


@register.simple_tag()
def kolibri_un_women_plugin_async_assets():
    """
    Using in a template will inject script tags that include the javascript assets defined
    by any concrete hook that subclasses UnWomenPluginSyncHook.
    :return: HTML of script tags to insert into kolibri_un_women_plugin/kolibri_un_women_plugin.html
    """
    return webpack_asset_render(hooks.UnWomenPluginAsyncHook, async=True)
