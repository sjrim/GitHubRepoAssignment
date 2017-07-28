from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.ninjas),
    url(r'^ninjas/(%P<color>\d+)$', views.ninjashow)
]