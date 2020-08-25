from django import urls
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from lazysignup.decorators import allow_lazy_user

from .models import Survey, Question, Choice, UserScore

@allow_lazy_user
def index(request, *args, **kwargs):
    surveys = Survey.objects.all()
    context = {
        'surveys' : surveys
    }
    return render(request, 'survey/index.html', context)

@allow_lazy_user
def new_guest_session(request):
    request.session.clear()
    return HttpResponseRedirect(urls.reverse('survey:index'))

@allow_lazy_user
def survey(request, survey_id, *args, **kwargs):

    if UserScore.objects.filter(survey__id=survey_id).exists():
        surveys = Survey.objects.all()
        return render(request, 'survey/index.html', {
            'surveys' : surveys,
            'error_message': "You have already taken this survey with this account. Create a new guest session to re-take the survey.",
        })
    else:
        survey = Survey.objects.get(pk=survey_id)
        questions = Question.objects.filter(survey=survey)
        points = 0

        if request.method == 'POST':

            for question in questions:
                selected = request.POST['survey']
                if selected == 'yes':
                    points=+1
            
            UserScore.objects.create(
                user = request.user,
                survey = survey,
                score = points,
            )

            return redirect('survey:results', survey_id)

        context = {
            'survey' : survey,
            'questions' : questions
        }
        return render(request, 'survey/survey.html', context)

@allow_lazy_user
def results(request, survey_id, *args, **kwargs):
    user = request.user

    context = {
        'survey' : Survey.objects.get(pk=survey_id),
        'score' : UserScore.objects.get(user__id=user.id, survey__id=survey_id)
    }
    return render(request, 'survey/results.html', context)