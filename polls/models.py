from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return   timezone.now() - datetime.timedelta(days=1)<=self.pub_date<=now
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
