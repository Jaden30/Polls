from django.contrib import admin

# Register your models here.

from .models import Question


# to register Questions in the admin site, to allow admin to be able to delete and add question etc
admin.site.register(Question)