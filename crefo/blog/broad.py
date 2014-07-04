# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.http import HttpResponse

from models import Entries, Categories, TagModel, CommentsModel

# template
from django.template import Context, loader

#exception
from django.http import Http404

# csrf
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
#decoration
from django.views.decorators.csrf import csrf_exempt

import md5

from util import util

#
#	category(blog)
#
def getCtgList ():
	return Categories.objects.all()

def getCtgCnt ():
	return len(Categories.objects.all())

#
#	broad
#
def byKeyword (word=''):
	""" get Broad list by Search Wordl """
	word = util.transStr(word)
	
	try:
		# 수정 필요 
		entries = Entries.objects.filter(title__contains=word).order_by('-created').values('id', 'title', 'readed', 'pop', 'created')
	except:
		#print 'error : findByWord Keyword[%s]' % word
		return False
	
	return entries

def byCategory (type=0):
	""" Find broad list by Category """
	type = util.transInt(type)
	if type > getCtgCnt() or type < 1 :return False;
	
	try:
		entries = Entries.objects.filter(category = type).order_by('-created').values('id', 'title', 'readed', 'pop', 'created')
	except:
		#print 'error : findByWord Keyword[%s]' % cateType
		return False
	
	return entries


#
#	content
#
def getEntriesById(pageId):
	"""Get Blog Page. (Defult(0) Is Latest Page.)"""
	print 'pageId>>>>>>>'
	print pageId
	pageId = util.transInt(pageId);
	
	try:
		if pageId != 0:
			entrie = Entries.objects.get(id = pageId)
		else:
			entrie = Entries.objects.latest('created')
	except:
		return False
	

	return entrie

#
#	etc
#
def getPop ():
	word = util.transStr(word)
	
	try:
		# 수정 필요 
		entries = Entries.objects.filter(title__contains=word).order_by('pop').values('id', 'title', 'readed', 'pop', 'created')
	except:
		#print 'error : findByWord Keyword[%s]' % word
		return False
	
	return entries
	
