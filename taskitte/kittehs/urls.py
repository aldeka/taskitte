from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^$', "kittehs.views.index"),
    (r'^(?P<list_pk>\d+)/$', "kittehs.views.list"),
)
