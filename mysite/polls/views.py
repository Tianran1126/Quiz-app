from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def result(request):
    return HttpResponse("you finish the quiz")

class Question_View(generic.ListView): 
    context_object_name='questions'
    template_name='polls/index.html'
    def get_queryset(self):
        return Question.objects.all()


class Option_View(generic.DetailView):
    model=Question
    template_name='polls/show_options.html'

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model=Question
    template_name='polls/detail.html'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def decision(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    num_questions=Question.objects.count()
    try:
      selected_option=question.option_set.get(pk=request.POST['option'])
    except:
        return render(request, 'polls/show_options.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    redirect_id=question_id+1 
    if (num_questions>=redirect_id):       
        return HttpResponseRedirect(reverse('quiz:option', args=(redirect_id,)))
    else:
        return HttpResponseRedirect(reverse('quiz:result')) 
           






