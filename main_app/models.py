from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Poll(models.Model):
  title = models.CharField(max_length=50)
  abstract = models.CharField(max_length=150)
  content = models.TextField(max_length=300)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'poll_id': self.id})