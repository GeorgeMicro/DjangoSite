from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
# Create your views here.
def index(request):
    return HttpResponse("Welcome to George's Wonderland!")

class PostView(generic.DetailView):
	model = Post;
	template_name = 'blog/post.html'