# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
	url(r'^page/(?P<pageId>\d+)/(?P<ctg>\d+)/(?P<subctg>\d+)/(?P<searchWord>\w*)/$', 'getPage'),
	url(r'^page/(?P<pageId>\d+)/(?P<ctg>\d+)/(?P<subctg>\d+)/$', 'getPage'),
	url(r'^page/(?P<pageId>\d+)/(?P<ctg>\d+)/$', 'getPage'),
	url(r'^page/(?P<pageId>\d+)/$', 'getPage'),
	url(r'^page/$', 'getPage'),
	
	url(r'^keyword/(?P<keyword>\w*)/(?P<broadNum>\d+)/$', 'broadByKeyword'),
	url(r'^ctg/$', 'getCategory'),

	url(r'^$', 'getPage'),
	)
