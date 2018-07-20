from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .views import signup,wallview,portfolioview,followview
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/gallery/index'}, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^(?P<username>[\w\-]+)/wall/$',wallview, name = 'wallview'),
    url(r'^(?P<username>[\w\-]+)/portfolio/$',portfolioview, name = 'portfolio'),
    url(r'^(?P<username>[\w\-]+)/follow/$',followview, name = 'follow'),
]