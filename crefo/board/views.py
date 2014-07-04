# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from board.models import Board
#from django.vies.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# Create your views here.

def testBoard(request):
	name = "Mike"
	html = "<html><body>Hi %s. this seems to have worked;</body></html>" % name
	return HttpResponse(html)


def search_form(request):
	return render_to_response('search_form.html')


def search(request):
	if 'q' in request.GET:	# 'q' 미 체크시 내용이 없을 시 KeyError 발생
		message = 'You searched for:' + request.GET['q']
	else:
		message = 'You submitted an empty form.'
	
	return HttpResponse(message)


def write_form(request):
	return render_to_response('test.html')