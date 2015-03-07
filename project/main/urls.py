from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^(?:home)?$', views.home, name='home'),
    url(r'^events$', views.get_events, name='events'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^resources$', views.resources, name='resources'),
)