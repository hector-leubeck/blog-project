from django.contrib import admin
from .models import Post


class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_author', 'post_date', 'post_category',
                    'post_pub')
    list_editable = ['post_pub']
    list_display_links = ['post_title']
    list_filter = ('post_author', 'post_category')


admin.site.register(Post, PostsAdmin)
