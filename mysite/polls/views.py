from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from .models import Question ,Option ,Set
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.core.cache import cache
# Create your views here.

def check(set_question):
    questions=set_question.question_set.all()
    correct=0
    for question in questions:
     if(question.selected_option==question.correct_option):
         correct+=1 
    return correct


def result(request):
    pk=0
    id=request.session['order']
    if(id/3==1):
        pk=1
    elif(id/3==2):
         pk=2
    set_question=get_object_or_404(Set,pk=pk) 
    correct=check(set_question) 
    Question.objects.update(selected_option=" ") 
    del request.session['order']
    return render(request,'polls/show_result.html',{'correct':correct})

class Set_View(generic.ListView): 
    context_object_name='sets'
    template_name='polls/index.html'
    def get_queryset(self):
        return Set.objects.all()

def handleSet(request):
    if '1' in request.POST:
     request.session['order']=1
    elif '2' in request.POST:
      request.session['order']=4
    return HttpResponseRedirect(reverse('quiz:option'))  

def optionView(request):
    question=get_object_or_404(Question,pk=request.session['order'])
    return render(request, 'polls/show_options.html', {
            'question': question
        })  



def selectOption(question_id,option_id):
    question=get_object_or_404(Question,pk=question_id) 
    selected_option=question.option_set.get(pk=option_id)
    question.selected_option=selected_option.option_text
    question.save()

def handle(request):
    if not 'option' in request.POST:
        return HttpResponseRedirect(reverse('quiz:option',))  
    else:    
     question_id=request.session['order'] 
     selectOption(question_id,request.POST['option'])
     if 'next' in request.POST:
        if (question_id % 3==0):
            return HttpResponseRedirect(reverse('quiz:result'))      
        else:
             redirect_id=question_id+1
             request.session['order']=redirect_id 
             return HttpResponseRedirect(reverse('quiz:option'))    
     elif 'previous' in request.POST:
         return previous(request, question_id)

def previous(request,question_id):
    if (question_id % 3!=1):
        redirect_id=question_id-1
        request.session['order']=redirect_id 
    return HttpResponseRedirect(reverse('quiz:option'))  







