# Create your views here.
# If using render shortcut libraries HttpResponse and loader aren't needed
# from django.http import HttpResponse
# from django.template import loader
#
# Writing in one line
# # from django.http import Http404
# # from django.shortcuts import render
# from django.shortcuts import Http404, render
#
# Using shortcut get_object_or_404() in detail()
from django.shortcuts import get_object_or_404, render

from .models import Question

# def index(request):
# 	return HttpResponse("Hello, world. You're at the polls index.")

# To refer to non-template index views check view.py.old
# Uncomment importation of loader and Httpresponse if uncommenting the code below
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_question_list': latest_question_list,
# 	}
# 	return HttpResponse(template.render(context, request))

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]		# what does the '[:5]' do ?
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

# After introducing get_object_or_404()
# def detail(request, question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question does not exist")
# 	return render(request, 'polls/detail.html', {'question': question})
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)