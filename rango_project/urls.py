from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from rango_app import views


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'rango.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^rango/', include('rango.rango_app.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}),
    )