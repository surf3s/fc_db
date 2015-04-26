from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'fc_db.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^populate_database/', 'fc_db.views.populate_database', name='populate_database'),
)
