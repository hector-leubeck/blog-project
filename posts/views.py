from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Case, When, Count, Q
from comments.forms import FormComment


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
    template_name = 'posts/post_search.html'

    def get_queryset(self):
        qs = super().get_queryset()
        searching = (self.request.GET.get('termo'))
        if not searching:
            return qs

        qs = qs.filter(Q(post_title__icontains=searching) |
                       Q(post_content__icontains=searching) |
                       Q(post_author__first_name__iexact=searching) |
                       Q(post_category__cat_name__iexact=searching))
        return qs


class PostCategories(PostIndex):
    template_name = 'posts/post_category.html'

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.kwargs.get('category')
        if not category:
            return qs
        qs = qs.filter(post_category__cat_name__iexact=category)
        return qs


class PostDetails(UpdateView):
    template_name = 'posts/post_details.html'
    model = Post
    form_class = FormComment
    context_object_name = 'post'
