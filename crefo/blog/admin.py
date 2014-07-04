# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Entries
from models import Categories
from models import TagModel

from models import TimeTest
# Register your models here.

class EntriesAdmin(admin.ModelAdmin):
	list_display = (u'id', u'title', u'created')
	pass

class TimeTestAdmin(admin.ModelAdmin):
	# DateTimeField 경우 auto_now_add, auto_now 옵션이 있을 경우 추가 불가
	# 이 경우 model에서 column.editable=True 설정으로 
	# 'classes': ['collapse'] 추가가 될 경우 접힌 상태로 둘 수 있다.
	#fields = ['test1']	
	"""
	fieldsets = [
		('test1', {'fields' : ['test1'], 'classes': ['collapse']})
	]
	"""
	pass

class CategorieAdmin(admin.ModelAdmin):
	pass

class TagAdmin(admin.ModelAdmin):
	pass

admin.site.register(Entries, EntriesAdmin)
admin.site.register(Categories, CategorieAdmin)
admin.site.register(TagModel, TagAdmin)

admin.site.register(TimeTest, TimeTestAdmin)