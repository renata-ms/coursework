from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', 'pollapp.views.index'),
                       (r'^(?P<poll_id>\d+)/$', 'pollapp.views.detail'),
                       (r'^(?P<poll_id>\d+)/results/$', 'pollapp.views.results'),
                       (r'^(?P<poll_id>\d+)/vote/$', 'pollapp.views.vote'),
                       (r'^admin/', include(admin.site.urls)),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, }),
                       )
