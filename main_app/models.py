from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Poll(models.Model):
  title = models.CharField(max_length=50)
  abstract = models.CharField(max_length=150)
  content = models.TextField(max_length=300)
  author = models.TextField(max_length=150,default = 0)
  hasVoted = models.TextField(
    max_length=3000,
    default = 0
    )
  published = models.BooleanField(default = False)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'poll_id': self.id})

class Response(models.Model):
  response = models.TextField(max_length=300)
  poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

class Question(models.Model):
  question = models.TextField(max_length=300)
  poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.question}"