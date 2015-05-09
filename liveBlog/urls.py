__author__ = 'mingyong'
from django.conf.urls import *
from models import Update

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list.ListView', {
        'queryset': Update.objects.all()
    }),
    url(r'^updates-after/(?P<id>\d+)/$', 'liveBlog.views.updates_after'),
)

