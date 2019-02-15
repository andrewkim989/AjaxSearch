from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^create$', views.create),
    url(r'^all$', views.all),
    url(r'^first/$', views.all),
    url(r'^first/(?P<num>\d+)$', views.first),
    url(r'^creature/(?P<num>\d+)$', views.onecreature),
    url(r'^creature/(?P<num>\d+)/edit$', views.edit),
    url(r'^creature/(?P<num>\d+)/delete$', views.delete),
    url(r'^creature/(?P<num>\d+)/deletetwo$', views.deletetwo),
    url(r'^search$', views.search),
    url(r'^alltwo$', views.alltwo),
    url(r'^searchcreatures$', views.searchresults)
]