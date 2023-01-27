from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'


class PostSearch(PostIndex):
    pass


class PostCategories(PostIndex):
    pass


class PostDetails(UpdateView):
    pass
