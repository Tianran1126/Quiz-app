from django.db import models

class Set(models.Model):
    id = models.IntegerField(primary_key=True)
    
class Question(models.Model):
    set=models.ForeignKey(Set,default=1, on_delete=models.CASCADE)
    question_text=models.CharField(max_length=1000)
    correct_option=models.CharField(max_length=100,)
    id = models.IntegerField(primary_key=True)
    selected_option=models.CharField(max_length=100,default="hello")
    def __str__(self):
        return self.question_text

class Option(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text= models.CharField(max_length=100)



    




