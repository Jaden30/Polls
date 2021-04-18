from django.urls import path 
from . import views 


urlpatterns = [
    # for polls.views.index 
    path('', views.IndexView.as_view(), name="index"),
    # for polls.views.details which is polls/question_id 
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    # for polls.views.results which is polls/question_id/results 
    path('<int:pk>/results/', views.ResultView.as_view(), name="results"),
    # for polls.views.vote which is polls/qiestion_id/vote
    path('<int:question_id>/vote/', views.vote, name ="vote"),
    ]