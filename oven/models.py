from __future__ import unicode_literals

from django.db import models

# Create your models here.
class  Cook(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    nick=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return (self.first_name+" "+self.last_name)
    
class Recipe(models.Model):
    cook=models.ManyToManyField(Cook)
    date=models.DateTimeField(auto_now_add=True)
    txt=models.CharField(max_length=100000)
    title=models.CharField(max_length=100,default=None)

    def __str__(self):
        return (self.title)

class Comment(models.Model):
    recipe=models.ForeignKey(Recipe)
    comment=models.CharField(max_length=400)
    date=models.DateTimeField(auto_now_add=True)

    def __str(self):
        return (self.title[0:30])
