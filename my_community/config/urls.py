# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

urlpatterns = []

if settings.DEBUG:
    urlpatterns.extend([
        url(
            r'^media/(?P<path>.*)$',
            serve,
            {'document_root': settings.MEDIA_ROOT}
        )
    ])

urlpatterns.extend([
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
])
