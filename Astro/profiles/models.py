from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=20000)

class Message(models.Model):
    value = models.TextField(max_length=1000000)
    date = models.DateField(default=datetime.now)
    user  = models.CharField(max_length=40)
    room = models.CharField(max_length=1000000)

class User(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=200)
    picture = models.ImageField()
    chat = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)

