import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse


# Create your tests here.
from .models import Question 


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self): 
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days ):
    time = timezone.now() - datetime.timedelta(days = days)
    return Question.objects.create(question_text=question_text, pub_date = time)


class QuestionIndexViewTests(TestCase):
    # functions for no question and the response you want it to show,
    def test_no_questions(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Np polls available ")
    
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        # QUESTIONS WIRH A PUB DATE IN THE PAST ARE DISPLAYED ON THE INDEX PAGE 
        question = create_question(question_text="Past Question", days=-30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['question'],)

    def test_future_question(self):
        # questions with pub date in the future should not be dispalyed on the index page 
        questiom = create_question(question_text= "Future question", days=30)
        response = self.client.get(reverse('index'))
        self.assertContains(response, "No polls are available ")
        self.assertQuerysetEqual(resonse.content['latest_question_list'], [])

    # tests for  future questions and past questions but only past question is displayed 
    def test_future_question_and_past_question(self):
        question = create_question(question_text="Future question", days=30,) 
        past= create_question(question_text="Past Question", days=-30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [past],
        )

    def test_twp_past_questions(self):
        question1 = create_question(question_text="Past Question", days=-30)
        question2 = create_question(question_text="Past Question", days=-30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question1, question2],
        )
