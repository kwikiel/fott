from django.conf.urls import patterns, url

from polls import views


urlpatterns = patterns ('',
        #pools/5
        url(r'^$', views.index, name='index'),
        url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
        #example thing that matches regex
        url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
        #example /polls/5/vote/
        url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
        
)
