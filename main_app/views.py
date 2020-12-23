from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Poll

def home(request):
  return render(request, 'home.html')

@login_required
def polls_index(request):
  polls = Poll.objects.all()
  return render(request, 'polls/index.html', {'polls': polls})

@login_required
def polls_detail(request, poll_id):
  poll = Poll.objects.get(id=poll_id)
  return render(request, 'polls/detail.html', {'poll': poll})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Failed to sign up'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
