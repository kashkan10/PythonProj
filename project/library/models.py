from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Book(models.Model):
    user=models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
