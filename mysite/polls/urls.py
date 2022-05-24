from django.urls import path 
from . import views

app_name='quiz'
urlpatterns=[path('',views.show_questions,name='vore')]