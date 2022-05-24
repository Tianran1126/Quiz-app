from django.db import models

class Question(models.Model):
    question_text=models.CharField(max_length=1000)
    def __str__(self):
        return self.question_text


class Option(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text= models.CharField(max_length=100)
    def __str__(self):
        return self.option_text


class CorrectOption(models.Model):
    option=models.OneToOneField(Option, on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.option.option_text




