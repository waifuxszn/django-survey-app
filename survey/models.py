from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    title       = models.CharField(max_length=100, default='Nursing Survey')
    length      = models.IntegerField(null=False)
    is_taken    = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Question(models.Model):
    question    = models.TextField(null=False)
    survey      = models.ForeignKey(Survey, related_name='survey', on_delete=models.CASCADE)

    def __str__(self):
        return "{content}".format(content=self.question) 

class Choice(models.Model):
    question    = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)

class UserScore(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    survey  = models.ForeignKey(Survey, on_delete=models.CASCADE)
    score   = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.score)