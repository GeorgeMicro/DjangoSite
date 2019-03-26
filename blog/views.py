from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
# Create your views here.
class PostView(generic.DetailView):
	model = Post;
	template_name = 'blog/post.html'

class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'post_list'
	
	def get_queryset(self):
		return Post.objects.all()