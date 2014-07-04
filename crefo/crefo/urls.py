# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
	# 관리자 사이트 문서를 활성화 시키기 위해 admin/doc 의 주석을 제거 해 주세요.:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	# 관리자 사이트를 활성화 시키기 위해 다음 줄의 주석을 제거 해 주세요.:
	url(r'^admin/', include(admin.site.urls)),

	#media
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'media'}),

    # custom
	url(r'^blog/', include('blog.urls')),
	url(r'^test/', include('board.urls')),

	url(r'^$', 'board.views.testBoard'),
)