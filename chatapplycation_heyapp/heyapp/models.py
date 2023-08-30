from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=1000)
    lastname = models.CharField(max_length=1000)
    dob = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

class Message(models.Model):
    message = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    sender = models.CharField(max_length=1000000)
    recever = models.CharField(max_length=1000000)