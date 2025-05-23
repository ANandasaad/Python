from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
     
     posts = Post.objects.all()
     print(posts.first())
     
     return render(request, 'index.html', {'posts': posts.first()})