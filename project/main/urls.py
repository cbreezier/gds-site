from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^(?:home)?$', views.home, name='home'),
    url(r'^events$', views.events, name='events'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^resources$', views.resources, name='resources'),
)