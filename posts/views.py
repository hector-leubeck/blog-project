from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView


class PostIndex(ListView):
    pass


class PostSearch(PostIndex):
    pass


class PostCategories(PostIndex):
    pass


class PostDetails(UpdateView):
    pass
