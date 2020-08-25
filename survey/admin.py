from django.contrib import admin

from .models import Survey, Question, UserScore

admin.site.site_url = "/survey"

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(UserScore)