from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.views.generic import TemplateView
from .views import createview,indexview,likeview,commentview,createcommentview
app_name = 'gallery'

urlpatterns = [
    url(r'^index$',indexview , name='index'),
    url(r'^create$',createview , name='create'),
    url(r'^(?P<id>\d+)/like/$',likeview, name='like'),
    url(r'^(?P<id>\d+)/comment/$',commentview, name='comment'),
    url(r'^(?P<id>\d+)/add/comment/$',createcommentview, name='commentpage')
    ]