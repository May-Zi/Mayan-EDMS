from __future__ import unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns('smart_settings.views',
    url(r'^list/$', 'setting_list', (), 'setting_list'),
)
