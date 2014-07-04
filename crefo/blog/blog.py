# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from models import Entries, Categories, TagModel, CommentsModel

from django.views.generic import View

# template
from django.template import Context, loader
# csrf
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
#decoration
from django.views.decorators.csrf import csrf_exempt

def blog (reqest, entry_id=0):
	entrie = Entries.objects.order_by('-created')[0:1]
	
	ctx = Context({
	'list_opt':'hide',
	'list_name':'',
	'title':entrie[0].title,
	'context':entrie[0].content,
	})
	ctx.update(csrf(request))

	return render_to_response('blog_read.html', ctx)


class Blog(View):
	def get (self, request, *args, **kwargs):
		if kwargs.get('page') == None:
			entrie = Entries.objects.order_by('-created')[0:1]
		else:
			entrie = Entries.objects.filter(id=int(kwargs.get('page')))
		
		ctx = Context({
		'list_opt':'hide',
		'list_name':'',
		'title':entrie[0].title,
		'context':entrie[0].content,
		})
		ctx.update(csrf(request))

		return render_to_response('blog_read.html', ctx)
"""
def blog (reqest, entry_id=0):
	if isinstance(entry_id, int):
		entry_id = 0
	
	if entry_id == 0:
		entrie = Entries.object.order_by('-created')
	else:
		entrie = Entries.object.filter(id = entry_id)
	
	ctx = Context({
	#'current_entry':current_entry,
	'list_name':'',
	'title':current_entry.title.,
	})
	ctx.update(csrf(request))

	return render_to_response('blog_read.html', ctx)
"""