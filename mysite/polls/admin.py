from django.contrib import admin 
from .models import Question, Option , Timer

class OptionInline(admin.TabularInline):
    model=Option
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['question_text']}),('The Correct option',{'fields':['correct_option']}),('The selected option',{'fields':['selected_option']}),('ID',{'fields':['id']})]
    inlines=[OptionInline]

admin.site.register(Question,QuestionAdmin)    
admin.site.register(Timer)

