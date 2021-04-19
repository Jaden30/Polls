from django.contrib import admin

# Register your models here.

from .models import Question, Choice


# to register Questions in the admin site, to allow admin to be able to delete and add question etc
class ChoiceInline(admin.TabularInline):
    model = Choice 
    extra = 3 


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date", "was_published_recently")
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)


