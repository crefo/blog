from django.conf.urls import patterns, include, url

urlpatterns = patterns('board.views',
	url(r'^search_form/$', 'search_form'),
	url(r'^search/$', 'search'),
	url(r'^write/$', 'write_form'),
	url(r'^$', 'testBoard'),
)