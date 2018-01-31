
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from kolibri.deployment.default.settings.base import *


if "kolibri_un_women_plugin" not in INSTALLED_APPS:
    INSTALLED_APPS += ["kolibri_un_women_plugin"]

LANGUAGES = [
    ('en', 'English')
]
