from django.conf.urls import patterns, include, url
from django.contrib import admin
from photoGallery.models import *
urlpatterns = patterns('',
    url(r'^$', 'simple.direct_to_template',
        kwargs={'template': '/photoGallery/index.html',
                'extra_context': {'item_list': lambda: Item.objecs.all()}
        },
    name="index"
    ),
     url(r'^items/$', 'list_detail.object_list',
        kwargs={
            'queryset': Item.objects.all(),
            'template_name': 'items_list.html',
            'allow_empty': True
        },
        name='item_list'
    ),
    url(r'^items/(?P<object_id>\d+)/$', 'list_detail.object_detail',
        kwargs={
            'queryset': Item.objects.all(),
            'template_name': 'items_detail.html'
        },
        name='item_detail'
    ),
    url(r'^photos/(?P<object_id>\d+)/$', 'list_detail.object_detail',
        kwargs={
            'queryset': Photo.objects.all(),
            'template_name': 'photos_detail.html'
        },
        name='photo_detail'
    ),
)
