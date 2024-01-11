from django.db import models

# Create your models here.

class Question(models.Model): # class가 table
    subject = models.CharField(max_length=200) # column , type
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject