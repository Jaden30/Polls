from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# DO NOT FORGET TO IMPORT THE MODELS CLASSES DESIGNED 
from .models import Question
from django.template import loader
# Create your views here.
def index(request):
    # create a list that is ordered by published date 
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # creating a dictionary, telling the template created to use the list created here 
    context = { "latest_question_list" : latest_question_list 
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    questio  = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/details.html", context)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on the question %s " % question_id)