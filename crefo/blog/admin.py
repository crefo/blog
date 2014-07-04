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
	# DateTimeField ��� auto_now_add, auto_now �ɼ��� ���� ��� �߰� �Ұ�
	# �� ��� model���� column.editable=True �������� 
	# 'classes': ['collapse'] �߰��� �� ��� ���� ���·� �� �� �ִ�.
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