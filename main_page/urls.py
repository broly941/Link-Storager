from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^create_link/$', views.create_link, name='create_link'),
    url(r'^tags/$', views.tags, name='tags'),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.tags_detail, name='tags_detail'),
    url(r'^link/(?P<pk>[0-9]+)/$', views.links_detail, name='links_detail'),
]
