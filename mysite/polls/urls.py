from django.urls import path 
from . import views 


urlpatterns = [
    # for polls.views.index 
    path('', views.index, name="index"),
    # for polls.views.details which is polls/question_id 
    path('<int:question_id>/', views.detail, name="details"),
    # for polls.views.results which is polls/question_id/results 
    path('<int:question_id>/results/', views.results, name="results"),
    # for polls.views.vote which is polls/qiestion_id/vote
    path('<int:question_id>/vote/', views.vote, name ="vote"),
    ]