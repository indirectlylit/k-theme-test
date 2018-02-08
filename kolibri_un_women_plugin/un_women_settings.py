
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from kolibri.deployment.default.settings.base import *


INSTALLED_APPS += ["social_django"]
AUTHENTICATION_BACKENDS += ['social_core.backends.google.GoogleOAuth2',
                            'social_core.backends.twitter.TwitterOAuth',
                            'social_core.backends.facebook.FacebookOAuth2']

if "kolibri_un_women_plugin" not in INSTALLED_APPS:
    INSTALLED_APPS += ["kolibri_un_women_plugin"]

SOCIAL_AUTH_URL_NAMESPACE = 'kolibri:user:social'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/learn'

# Default pipeline methods
SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'kolibri_un_women_plugin.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
]

LANGUAGES = [
    ('en', 'English')
]

# Social Auth Keys and Secrets
SOCIAL_AUTH_TWITTER_KEY = os.environ.get('KOLIBRI_SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get('KOLIBRI_SOCIAL_AUTH_TWITTER_SECRET')
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('KOLIBRI_SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('KOLIBRI_SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('KOLIBRI_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('KOLIBRI_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
