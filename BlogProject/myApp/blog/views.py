from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post




# Create your views here.
def home(request):
  #load all the post from db(10)
  posts = Post.objects.all()[:11]
  
  #print (post)
  data = {
    'posts' : posts
  }
  
  
  return render(request, 'home.html',  data)
