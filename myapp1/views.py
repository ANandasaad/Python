from django.shortcuts import render , redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    features = Feature.objects.all()
    for feature in features:
        print(f"Heading: {feature.heading}")
        print(f"Subheading: {feature.subHeading}")
        print(f"Description: {feature.desc}")
        print("-" * 50)
    return render(request, 'index.html', {'feature': features.first()})


def counter(request):
    words= request.POST['words']
    countWord= len(words.split())
    return render(request, 'counter.html', {'count': countWord} )

def register(request):
    
    if request.method == 'POST':
        
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        confirm_password= request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exists')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
                
        else:
            messages.info(request, 'Password is not same')
            return redirect('register')       
        
        
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
    
   
   
   
def logout(request):
    auth.logout(request)
    return redirect('index')