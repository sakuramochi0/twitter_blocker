from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^connect/$', views.connect, name='connect'),
    url(r'^callback/$', views.callback, name='callback'),
    url(r'^blocked/$', views.blocked, name='blocked'),
]
