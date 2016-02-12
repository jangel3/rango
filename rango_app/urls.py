from django.conf.urls import patterns, url
from rango_app import views


urlpatterns = patterns('',
                       url(r'^$',views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^add_category/$', views.add_category, name='add_category'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)[/]?$', views.category, name='category'),
                       url(r'^.+[/]?', views.page_not_found, name='page_not_found')  # This MUST appear last in the
                       # patterns
                       )
