from datetime import datetime
from django.conf.urls import patterns, url
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'votes.views.home', name='home'),
    url(r'^home2', 'votes.views.home2', name='home2'),
    url(r'^home', 'votes.views.home', name='home'),

    url(r'^contact$', 'votes.views.contact', name='contact'),
    url(r'^about', 'votes.views.about', name='about'),
    
)
