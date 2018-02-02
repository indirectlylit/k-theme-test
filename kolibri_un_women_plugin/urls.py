from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'', include('social_django.urls', namespace='social')),
    url(r'^$', views.UserView.as_view(), name='user'),
]
