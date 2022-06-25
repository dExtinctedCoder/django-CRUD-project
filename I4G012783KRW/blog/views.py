from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from . models import Post
# Create your views here.


class PostCreateView(CreateView):
  model = Post
  fields = Post.objects.all()
  success_url = reverse_lazy("blog:all")


class PostUpdateView(UpdateView):
  model = Post
  fields = Post.objects.all()
  success_url = reverse_lazy("blog:all")


class PostDeleteView(DeleteView):
  model = Post
  fields = Post.objects.all()
  success_url = reverse_lazy("blog:all")


class PostListView(ListView):
  model = Post
  # fields = Post.objects.all()


class PostDetailView(DeleteView):
  model = Post
  # fields = Post.objects.all()