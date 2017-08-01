from django.conf.urls import url,include 
from django.contrib import admin

#admin.autodiscover()
from .import views


app_name = 'blog'
urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
   url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
   url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
   url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
]
