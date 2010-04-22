from django.db import models
from django.contrib.auth.models import User

class Sprint(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __unicode__(self):
        return self.name

class Story(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    sprint = models.ForeignKey(Sprint, blank=True, null=True)

    def __unicode__(self):
        return self.name

CATEGORIES = (
('b', 'BUG'),
('t', 'TASK'),
('r', 'RESEARCH'),
('d', 'DESIGN'),
)
class TaskCategory(models.Model):
    name = models.CharField(max_length=16, choices=CATEGORIES)

    def __unicode__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    estimate = models.IntegerField()
    remaining = models.IntegerField()
    actual = models.IntegerField()
    reporter = models.ForeignKey(User, related_name='reporter')
    assigned = models.ForeignKey(User, related_name='assigned', blank=True, null=True)
    story = models.ForeignKey(Story)

    def __unicode__(self):
        return self.name
