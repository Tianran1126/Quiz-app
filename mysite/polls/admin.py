from django.contrib import admin 
from .models import Question, Option ,Set


class QuestionInline(admin.TabularInline):
    model=Question
    extra=4
class OptionInline(admin.TabularInline):
    model=Option
    extra=3
class SetAdmin(admin.ModelAdmin):
    fieldset=[('The Set_ID',{'fields':['id']})]
    inlines=[QuestionInline]    

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['question_text']}),('The Correct option',{'fields':['correct_option']}),('The selected option',{'fields':['selected_option']}),('ID',{'fields':['id']})]
    inlines=[OptionInline]

   
admin.site.register(Set,SetAdmin)
admin.site.register(Question,QuestionAdmin)