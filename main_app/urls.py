from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('polls/', views.polls_index, name='index'),
  path('polls/<int:poll_id>/', views.polls_detail, name='detail'),
  path('polls/create/', views.PollCreate.as_view(), name='polls_create'),
  path('accounts/signup/', views.signup, name='signup'),
]