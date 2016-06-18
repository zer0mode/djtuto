from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /polls/
    url(r'^$', views.index, name='index'),
	# the 'name' value as called by the {% url %} template tag	
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),		# ex: /polls/5/
	# all the URL modifications can be done in urls.py > hardcoded urls shouldn't be present in templates
	# added the word 'specifics'
	url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),    
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]