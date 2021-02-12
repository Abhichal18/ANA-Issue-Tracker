from django.contrib import admin
from .models import CustomUser, questions,askquestions
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(questions)
admin.site.register(askquestions)