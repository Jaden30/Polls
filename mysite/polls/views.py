from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# DO NOT FORGET TO IMPORT THE MODELS CLASSES DESIGNED 
from .models import Question, Choice
from django.template import loader
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list" 
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
  

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"

class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


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