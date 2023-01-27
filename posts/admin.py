from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostsAdmin(SummernoteModelAdmin):
    list_display = ('post_title', 'post_author', 'post_date', 'post_category',
                    'post_pub')
    list_editable = ['post_pub']
    list_display_links = ['post_title']
    list_filter = ('post_author', 'post_category')
    summernote_fields = ('post_content', )


admin.site.register(Post, PostsAdmin)
