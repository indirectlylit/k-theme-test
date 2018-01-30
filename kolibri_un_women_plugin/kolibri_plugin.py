from __future__ import absolute_import, print_function, unicode_literals
from kolibri.core.webpack import hooks as webpack_hooks
from kolibri.plugins.base import KolibriPluginBase
from . import hooks, urls


class UnWomenPlugin(KolibriPluginBase):
    def url_module(self):
        return urls

    def url_slug(self):
        return "^kolibri_un_women_plugin/"




class UnWomenPluginAsset(webpack_hooks.WebpackBundleHook):
    unique_slug = "kolibri_un_women_plugin_module"
    src_file = "assets/src/app.js"
    



