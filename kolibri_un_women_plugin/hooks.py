from __future__ import absolute_import, print_function, unicode_literals
from kolibri.core.webpack import hooks as webpack_hooks


class UnWomenPluginSyncHook(webpack_hooks.WebpackInclusionHook):
    """
    Inherit a hook defining assets to be loaded synchronously in kolibri_un_women_plugin/kolibri_un_women_plugin.html
    """

    class Meta:
        abstract = True


class UnWomenPluginAsyncHook(webpack_hooks.WebpackInclusionHook):
    """
    Inherit a hook defining assets to be loaded asynchronously in kolibri_un_women_plugin/kolibri_un_women_plugin.html
    """

    class Meta:
        abstract = True
