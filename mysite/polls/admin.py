from django.contrib import admin 
from .models import Question ,Option 

class OptionInline(admin.TabularInline):
    model=Option
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['question_text']}),('The Correct option',{'fields':['correct_option']})]
    inlines=[OptionInline]

admin.site.register(Question,QuestionAdmin)    

