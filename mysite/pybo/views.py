from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answer
# Create your views here.


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'pybo/question_detail.html', {'question' : question})

    
