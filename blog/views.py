"""
    blog/views.py
    -------------
"""
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from .models import Post


class BlogCreateView(CreateView):
    """ C: Create a new blog post. """
    model = Post
    template_name = 'new.html'
    fields = '__all__'


class BlogListView(ListView):
    """ R: A blog list view for displaying all posts. """
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    """ R: A blog detail view for displaying single post. """
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'


class BlogUpdateView(UpdateView):
    """ U: Update a post. """
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'body', 'author']


class BlogDeleteView(DeleteView):
    """ D: Delete a post. """
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
