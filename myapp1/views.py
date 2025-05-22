from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Feature

# Create your views here.

def index(request):
    feature1= Feature()
    feature1.id=0;
    feature1.heading='Liberty NFT Market'
    feature1.subHeading='Create, Sell & Collect Top NFT'
    feature1.desc="Liberty NFT Market is a really cool and professional design for your NFT websites. This HTML CSS template is based on Bootstrap v5 and it is designed for NFT related web portals. Liberty can be freely downloaded from TemplateMo's free css templates"
    return render(request, 'index.html', {'feature':feature1})


def counter(request):
    words= request.POST['words']
    countWord= len(words.split())
    return render(request, 'counter.html', {'count': countWord} )

