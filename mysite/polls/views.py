from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from .models import Question ,Option ,Timer
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.core.cache import cache
# Create your views here.

def result(request):
    del request.session['order']
    return HttpResponse("Well done")

class Question_View(generic.ListView): 
    context_object_name='questions'
    template_name='polls/index.html'
    def get_queryset(self):
        return Question.objects.all()


def optionView(request):
    if  not ('order' in request.session):
      request.session['order']=1 
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
    question_id=request.session['order']
    if not 'option' in request.POST:
        question=get_object_or_404(Question,pk=question_id)
        return HttpResponseRedirect(reverse('quiz:option',))  
    elif 'next' in request.POST:
        selectOption(question_id,request.POST['option'])
        redirect_id=question_id+1
        request.session['order']=redirect_id 
        num_questions=Question.objects.count()
        if (num_questions>=redirect_id):
            return HttpResponseRedirect(reverse('quiz:option'))      
    elif 'previous' in request.POST:
         return previous(request, question_id,request.POST['option'])




def previous(request,question_id,option_id):
    selectOption(question_id,option_id)
    if(question_id>=1):
        redirect_id=question_id-1
        request.session['order']=redirect_id 
        print( request.session['order'])
        return HttpResponseRedirect(reverse('quiz:option'))  

"""
def decision(request,question_id):
    timer=get_object_or_404(Timer,pk=1)      
    timer.timer=(request.POST['timer'])
    timer.save()  
    try:
        correct=Correct.objects.get(pk=1)
    except Correct.DoesNotExist:
         correct=Correct()
         correct.save()
    correct=Correct.objects.get(pk=1)     
    selected_option=Option()
    question=get_object_or_404(Question,pk=question_id)
    num_questions=Question.objects.count()
    try:
      selected_option=question.option_set.get(pk=request.POST['option'])
    except:
        return render(request, 'polls/show_options.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })   
    
    if(selected_option.option_text==question.correct_option):
           correct.correct_answer+=1
           correct.save()    
    redirect_id=question_id+1 
    if (num_questions>=redirect_id):
        return HttpResponseRedirect(reverse('quiz:option', args=(redirect_id,)))
    else:
        return HttpResponseRedirect(reverse('quiz:result')) 
"""
           






