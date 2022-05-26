from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.views import generic
# Create your views here.

def show_questions(request):
    return HttpResponse("Here all the questions")

class Question_View(generic.ListView): 
    context_object_name='questions'
    template_name='polls/index.html'
    def get_queryset(self):
        return Question.objects.all()
