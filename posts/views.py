from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Case, When, Count


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs.order_by('-id').filter(post_pub=True)
        qs.annotate(
            comments_pub=Count(Case(When(comments__com_pub=True, then=1))))
        return qs


class PostSearch(PostIndex):
    template_name = 'post/post_search.html'


class PostCategories(PostIndex):
    template_name = 'posts/post_category.html'


class PostDetails(UpdateView):
    pass
