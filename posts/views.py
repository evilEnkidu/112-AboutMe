from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView
)
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]
    success_url = reverse_lazy('list')  # This is the key change