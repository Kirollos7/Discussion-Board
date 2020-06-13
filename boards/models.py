from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Board(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(unique=True, null=True, max_length=50,help_text='Enter Name of Category.')
    description = models.TextField(null=True, max_length=2000, help_text='Enter Description of Category.')

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=500,null=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete = models.CASCADE)
    created_by = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    
    
class Post(models.Model):
    message = models.TextField(max_length=10000, null=True)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete = models.CASCADE) 
    created_by = models.ForeignKey(User, related_name='posts' , on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add= True)
    