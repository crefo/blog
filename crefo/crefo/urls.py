# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
	# ������ ����Ʈ ������ Ȱ��ȭ ��Ű�� ���� admin/doc �� �ּ��� ���� �� �ּ���.:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	# ������ ����Ʈ�� Ȱ��ȭ ��Ű�� ���� ���� ���� �ּ��� ���� �� �ּ���.:
	url(r'^admin/', include(admin.site.urls)),

	#media
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'media'}),

    # custom
	url(r'^blog/', include('blog.urls')),
	url(r'^test/', include('board.urls')),

	url(r'^$', 'board.views.testBoard'),
)