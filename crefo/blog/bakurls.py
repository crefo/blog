# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView

from viewTest import BlogTest
from blog import Blog
from blog import blog

blogtest = BlogTest()
print "test ing"
urlpatterns = patterns('blog.views',
	url(r'^ajax/add/$', 'view.add_todo'),
	url(r'^ajax/more/$', 'view.more_todo'),

	#url(r'^page/$', 'index'),
	#url(r'^page/(?P<page>\d+)/$', 'index'),
	url(r'^entry/(?P<entry_id>[0-9]*)$', 'read'),
	url(r'^write/$', blogtest.write_form),

    url(r'^add/post/$', 'add_post'),
	url(r'^add/comment$', 'add_comment'),
	url(r'^del/comment$', 'del_comment'),
	url(r'^get/comments/(?P<entry_id>\d+)/$', 'get_comments'),

	url(r'^test/$', 'write_test'),
	url(r'^testresult/$', 'write_test_result'),

	url(r'^readtest/$', 'readtest'),
	
	url(r'^tt/$', 'blog'),

    url(r'', Blog.as_view(), name='Blog'),
	
	url(r'^page/(?P<page>\d+)/$', Blog.as_view(), name='Blog'),
	url(r'', Blog.as_view(), name='Blog'),
	#url(r'^$', 'index'),
	#url(r'', TemplateView.as_view(template_name='main/index.html')),
)
