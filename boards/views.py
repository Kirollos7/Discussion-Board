from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})


def boards_topics(request, board_id):
    try:
        b = Board.objects.get(pk=board_id)
    except Board.DoesNotExist:
        return render(request,'error.html',{'b':b})
    return render(request, 'topics.html',{'b':b})