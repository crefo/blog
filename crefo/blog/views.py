# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

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

import json

# Create your views here.
from . import broad
from util import util

# 한글 입력 관련 ascii to utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


BLOG_NAME='Crefo Home'
PAGE_CNT =util.PAGE_CNT


def getPage (request, pageId=0, ctg='', subctg='', searchWord=''):
	pageId = util.transInt(pageId)
	ctg = util.transInt(ctg)
	subctg = util.transInt(subctg)
	searchWord = util.transStr(searchWord)
	
	entrie = broad.getEntriesById(pageId)
	cnt = {
	'title':entrie.title,
	'ctg':ctg,
	'subctg':subctg,
	'keyword' : searchWord,
	'context':entrie.content,
	'result': entrie is not False
	}
	#print cnt['ctg']
	
	ctx = Context(cnt)
	ctx.update(csrf(request))
	return render_to_response('blog_read.html', ctx)


#
## Broad
#
def broadByKeyword (request, keyword='', broadNum=0):
	#print 'keyword : ' + keyword + '  pages : ' + str(broadNum)
	broadNum = util.transInt(broadNum);
	broadData = broad.byKeyword(keyword)

	cont={}
	cont['result'] = broadData is not False

	if request.is_ajax():
		broadInfo={}
		datas=[]
		startNum, endNum = util.getInterval(broadData.count(), broadNum - 1)
		#print "startNum %d endNum %d " %(startNum, endNum)
		for i in range( endNum - startNum) :
			entriesNum = i + startNum
			entrie = broadData[entriesNum]
			datas.append({'num':entriesNum, 'id': entrie['id'], 'title':entrie['title'], 'readed':entrie['readed'], 'pop': entrie['pop'], 'created':entrie['created'].strftime("%Y-%m-%d")});
		
		broadCnt = broadData.count() / PAGE_CNT
		if broadData.count() % PAGE_CNT > 0 :
			broadCnt += 1

		broadInfo['broad'] =datas
		broadInfo['broadCnt']=broadCnt

		result = json.dumps(broadInfo)
		return HttpResponse(result, content_type='application/json')
	else:
		"""
			if use not ajax 
		"""
		print "is not ajax"
		pass

	return HttpResponse('error')


def getCategory (request):
	ctgs = broad.getCtgList()

	if request.is_ajax():
		datas = []
		for ctg in ctgs:
			datas.append({'ctgName': ctg.title, 'cnt': len(broad.byCategory(ctg.id))})
		
		result = json.dumps(datas)
		return HttpResponse(result, content_type='application/json')
	else:
		"""
			if use not ajax 
		"""
		print "is not ajax"
		pass

	return HttpResponse('error')


def getPop (request):
	broadData = broad.getPop()

	cont={}
	cont['result'] = broadData is not False

	if request.is_ajax():
		broadInfo={}
		datas=[]
		startNum, endNum = util.getInterval(broadData.count(), broadNum - 1)
		#print "startNum %d endNum %d " %(startNum, endNum)
		for i in range( endNum - startNum) :
			entriesNum = i + startNum
			entrie = broadData[entriesNum]
			datas.append({'num':entriesNum, 'id': entrie['id'], 'title':entrie['title'], 'readed':entrie['readed'], 'pop': entrie['pop'], 'created':entrie['created'].strftime("%Y-%m-%d")});
		
		broadCnt = broadData.count() / PAGE_CNT
		if broadData.count() % PAGE_CNT > 0 :
			broadCnt += 1

		broadInfo['broad'] =datas
		broadInfo['broadCnt']=broadCnt

		result = json.dumps(broadInfo)
		return HttpResponse(result, content_type='application/json')
	else:
		"""
			if use not ajax 
		"""
		print "is not ajax"
		pass

	return HttpResponse('error')