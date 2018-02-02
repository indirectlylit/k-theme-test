from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ccthin/manifest.xml$', views.ThinCommonCartridgeManifestView.as_view(), name='thinccmanifest'),
]
