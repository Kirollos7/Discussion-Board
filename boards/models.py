from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
# Create your models here.


class Board(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(unique=True, null=True, max_length=50,help_text='Enter Name of Category.')
    description = models.TextField(null=True, max_length=2000, help_text='Enter Description of Category.')

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_dt').first()

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=500,null=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete = models.CASCADE)
    created_by = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0,null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    updated_dt = models.DateTimeField(null=True)

    def __str__(self):
        return self.subject

class Post(models.Model):
    message = models.TextField(max_length=10000, null=True)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete = models.CASCADE) 
    created_by = models.ForeignKey(User, related_name='posts' , on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add= True)
    updated_by = models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)
    updated_dt = models.DateTimeField(null=True)

    def __str__(self):
        truncted_message = Truncator(self.message)
        return truncted_message.chars(30)
    