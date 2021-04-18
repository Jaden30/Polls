from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# DO NOT FORGET TO IMPORT THE MODELS CLASSES DESIGNED 
from .models import Question, Choice
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
    question  = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question" : question})

def results(request, question_id):
    question = get_object_or_404(Question , pk=question_id)
    return render(request, "polls/results.html", {"question" : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        # request.POST response is a dictionary objects that lets you access submitted data by keyname 
        # it returns the id of a selected choice as string 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form 
        return render(request, "polls/details.html",
         {"question": question
        , 
        "error message " : "You did not select a choice ", })
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        # always return a HTTP RESPONSE REDIRECT after using a request.POST[]
        # THIS REDIRECTS TO THE RESULT SECTION OF THE VOTED QUESTION
        return HttpResponseRedirect(reverse('results', args=(question.id,)))