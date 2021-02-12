from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True, default=0)


class questions(models.Model):
    options=[
            ("hostels","Hostels"),
            ("academics","Academics"),
            ]
    category=models.CharField(choices=options,max_length=20,default=0)
    question = models.CharField(max_length=200)
    answer=models.TextField()

    def __str__(self):
        return self.question
    
class askquestions(models.Model):
    options=[
            ("hostels","Hostels"),
            ("academics","Academics"),
            ]
    category=models.CharField(choices=options,max_length=20,default=0)
    question = models.CharField(max_length=200)
    def __str__(self):
        return self.question