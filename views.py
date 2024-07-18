from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'object_list'
    ordering = ['-date']
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
