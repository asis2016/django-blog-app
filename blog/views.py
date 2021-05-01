from django.views.generic import ListView, DetailView

from .models import Post


class BlogListView(ListView):
    """ A blog list view for displaying all posts. """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    """ A blog detail view for displaying single post. """
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'