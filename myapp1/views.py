from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    context = {
        'name': "Anand",
        "age": "21",
        'nationality':"Indian"
    }
    return render(request, 'index.html')


def counter(request):
    words= request.POST['words']
    countWord= len(words.split())
    return render(request, 'counter.html', {'count': countWord} )

