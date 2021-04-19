from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    # fields in the database for the table Question
    question_text = models.CharField(max_length=600)
    pub_date = models.DateTimeField('date published')
    # a string representation of the object
    def __str__(self):
        return self.question_text
    # a way to calculate when it was published 

    @admin.display(
        boolean=True, 
        ordering='pub_date',
        description ="Published recently",


    )
    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    

    def __str__(self):
        return self.choice_text