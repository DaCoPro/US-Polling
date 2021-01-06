from django.forms import ModelForm
from .models import Question
from .models import Response

class QuestionForm(ModelForm):
  class Meta:
    model = Question
    fields = ['question']

class ResponseForm(ModelForm):
  class Meta:
    model = Response
    fields = ['response']