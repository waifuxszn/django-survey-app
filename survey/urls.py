  
from django.conf.urls import url

from . import views
#from . import admin_views


app_name = 'survey'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_guest_session/$', views.new_guest_session, name='new_guest_session'),
    url(r'^(?P<survey_id>[0-9]+)/take_survey/$', views.survey, name='survey'),
    url(r'^(?P<survey_id>[0-9]+)/survey_results/$', views.results, name='results')
    #url(r'^admin/polls/results$', admin_views.results, name='results'),
]