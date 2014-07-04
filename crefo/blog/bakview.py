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

per_page = 3

# Create your views here.

def index (request, page=1):
	if isinstance(page, int):
		page = 1
	else:
		page = int(page)
	#page = int(page)	# 인자 값(page)은 unicode 값이라서 정수형으로 변환이 필요하다.

	start_pos = (page-1) * per_page
	end_pos = start_pos + per_page	

	page_title = '블로그 글 목록 화면'

	entries = Entries.objects.all()[start_pos:end_pos]
	"""
		#entries = Entries.objects.all().order_by('FIELDNAME')[start_pos:end_pos]
		#entries = Entries.objects.all().order_by('-FIELDNAME')[start_pos:end_pos]

		# 연관된 자료 까지 불러온다 ex 댓글
		# https://docs.djangoproject.com/en/dev/ref/models/querysets/
		#entries = Entries.objects.all().select_related('tags').order_by('-created')[start_pos:end_pos]

		# string의 내장 메소드 '.encode('utf-8'))'의 적용은 html 문서에서 영문 외의 문자의 경우
		# 문제가 발생할 수 있다. 이 경우 utf-8 으로 인코딩함으로 해결할 수 이다.
		
		#return HttpResponse('안녕, 여러분, [%s] 글은 첫 번째 글이야.' % entries[0].title.encode('utf-8'))
	"""
	#templates
	#tpl = loader.get_template('list.html')
	ctx = Context({
	'page_title':page_title,
	'entries':entries,
	'current_page':page
	})
	
	ctx.update(csrf(request))

	return render_to_response('list.html', ctx)
	

def read (request, entry_id):
	# 한글 사용을 위해서는 utf-8 설정을 문서 상단과 저장 시 등록하여야 한다
	# id의 경우 생성 시 부여하는 숫자로 삭제 시 해당 번호는 공란이 된다.!!

	page_title = '블로그 글 화면'
	if isinstance(entry_id, int):
		entry_id = 1
	
	"""
		entrieCnt = Entries.objects.count()
		if entrieCnt <= entry_id or entrieCnt < 0 :
			return HttpResponse('warring Max count [%d] your choise [%d]' % (entrieCnt - 1, entry_id))
	"""
	"""
		#해당하는 row 선택
		#current_entry = Entries.objects.get(id=int(entry_id))
		#column 선택
		#print Entries.objects.values('id', 'title')
		#중복제거
		#Entry.objects.order_by('pub_date').distinct('pub_date')
		# except 체크
		from django.core.exceptions import ObjectDoesNotExist
		try:
			e = Entry.objects.get(id=3)
			b = Blog.objects.get(id=1)
		except ObjectDoesNotExist:
			print("Either the entry or blog doesn't exist.")
	"""
	try:
		current_entry = Entries.objects.get(id=entry_id)
	except Entries.DoesNotExist:
		raise Http404

	try:
		prev_entry = current_entry.get_previous_by_created()
	except:
		prev_entry = None
	try:
		next_entry = current_entry.get_next_by_created()
	except:
		next_entry = None

	#print 'current_entery.id = [%d]' % (current_entry.id)
	#return HttpResponse('안녕, 여러분. [%d]번 글은 [%s]이야.' % (current_entry.id, current_entry.title.encode('utf-8')))
	
	comments = CommentsModel.objects.filter(entry=current_entry).order_by('created')

	ctx = Context({
	'page_title':page_title,
	'current_entry':current_entry,
	'prev_entry':prev_entry,
	'next_entry':next_entry,
	'comments':comments
	})
	ctx.update(csrf(request))

	return render_to_response('read.html', ctx)

def write_form(request):
	page_title= '블로그 글 쓰기 화면'
	categories = Categories.objects.all()

	ctx = Context({
	'page_title':page_title,
	'categories':categories
	})
	ctx.update(csrf(request))
	return render_to_response('write.html', ctx)

def add_post (request):
    # 글 제목 처리
    if request.POST.has_key('title') == False:
        return HttpResponse('글 제목을 입력해야 한다우.')
    else:
        if len(request.POST['title']) == 0:
            return HttpResponse('글 제목엔 적어도 한 글자는 넣자!')
        else:
            entry_title = request.POST['title']

    # 글 본문 처리
    if request.POST.has_key('content') == False:
        return HttpResponse('글 본문을 입력해야 한다우.')
    else:
        if len(request.POST['content']) == 0:
            return HttpResponse('글 본문엔 적어도 한 글자는 넣자!')
        else:
            entry_content = request.POST['content']

    # 글 갈래 처리
    if request.POST.has_key('category') == False:
        return HttpResponse('글 갈래를 골라야 한다우.')
    else:
        try:
            entry_category = Categories.objects.get(id=request.POST['category'])
        except:
            return HttpResponse('이상한 글 갈래구려')

    # 글 꼬리표 처리
    if request.POST.has_key('tags') == True:
        tags = map(lambda str: str.strip(), unicode(request.POST['tags']).split(','))
        tag_list = map(lambda tag: TagModel.objects.get_or_create(title=tag)[0], tags)
    else:
        tag_list = []
    
    # 꼬리표 저장을 위해 임시 저장
    new_entry = Entries(title=entry_title, content=entry_content, category=entry_category)
    try:
        new_entry.save()
    except:
        return HttpResponse('글을 써넣다가 오류가 발생했습니다.')
    
    # 꼬리표 추가
    for tag in tag_list:
        new_entry.tags.add(tag)
        
    # 최종 저장.
    if len(tag_list) > 0:
        try:
            new_entry.save()
        except:
            return HttpResponse('글을 써넣다가 오류가 발생했습니다.')

    return HttpResponse('%s번 글을 제대로 써넣었습니다.' % new_entry.id)


def add_comment(request):
	# writer name 
	"""
		if request.POST.has_key('name') == False:
			return HttpResponse('글쓴이 이름을 입력해야 한다우.')
		else:
			if len(request.POST['name'] == 0:
				return HttpResponse('글쓴이 이름을 입력해야 한다우.')
			else:
				cmt_name = request.POST['name']
	"""
	cmt_name = request.POST.get('name','')
	if not cmt_name.strip() :
		return HttpResponse('글쓴이 이름을 입력해야 한다우.')
	
	# password
	cmt_password = request.POST.get('password','')
	if not cmt_password.strip() :
		return HttpResponse('비밀번호를 입력해야 한다우.')
	cmt_password = md5.md5(cmt_password).hexdigest()
	
	# comment
	cmt_content = request.POST.get('content','')
	if not cmt_content.strip() :
		return HttpResponse('댓글 내용을 입력해야 한다우.')	
	
	# Comment is included in content check
	cmt_id = request.POST.get('entry_id', '')
	if not cmt_id.strip() :
		return HttpResponse('댓글 달 글을 지정해야 한다우.')
	else:
		try:
			entry = Entries.objects.get(id=cmt_id)
		except:
			return HttpResponse('그런 글은 없지롱')
	
	try:
		new_cmt = CommentsModel(name=cmt_name, pwd=cmt_password, content=cmt_content, entry=entry)
		new_cmt.save()
		
		entry.comments += 1
		entry.save()
		
		return HttpResponse('성공')
	except :
		return HttpResponse('제대로 저장하지 못했습니다.')
	return HttpResponse('문제가 생겨 저장하지 못했습니다.')


def del_comment(request):
	cmt_id = request.POST.get('comment_id','')

	# get comment
	if not cmt_id.strip():
		return  HttpResponse("댓글 들 글을 지정해야 한다우.")
	else:
		try:
			cmt = CommentsModel.objects.get(id=cmt_id, pwd=md5.md5(request.POST['comment_del_pwd']).hexdigest())
		except:
			return HttpResponse("비밀번호가 틀렀습니다.")
	
	print len(CommentsModel.objects.filter(entry=cmt.entry))

	entry = cmt.entry
	entry.comments = len(CommentsModel.objects.filter(entry=cmt.entry)) -1
	entry.save()

	cmt.delete()
	
	return HttpResponse("삭제 완료")
	

def get_comments (reqest, entry_id=None):
	print "is_ajax >> %d " % int(reqest.is_ajax())
	print entry_id
	if reqest.is_ajax():
		with_layout = False
	else:
		with_layout = True

	comments = CommentsModel.objects.filter(entry=entry_id).order_by('created')
	tpl = loader.get_template('comments.html')
	ctx = Context({
	'comments':comments,
	'with_layout':with_layout
	})

	return HttpResponse(tpl.render(ctx))
	
def more_todo(request):
    if request.is_ajax():
        todo_items = ['Mow Lawn', 'Buy Groceries',]
        data = json.dumps(todo_items)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404


def add_todo(request):
	print request.is_ajax()
	print request.POST

	if request.is_ajax():
		data = {'message': "%s added" % request.POST.get('item')}
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def write_test (request):
	ctx = Context({})
	ctx.update(csrf(request))
	return render_to_response('write_test.html', ctx)

def write_test_result (request):
	print request.POST.get('content')
	return HttpResponse(request.POST.get('content'));

def readtest (request):
	ctx = Context({
	'page_title':'test',
	'list_name':'list_name',
	'title':'title',
	})
	ctx.update(csrf(request))
	return render_to_response('blog_read.html', ctx);
	