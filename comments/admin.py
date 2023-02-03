from django.contrib import admin
from .models import Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('com_name', 'com_post', 'com_date')
    list_display_links = ['com_name', 'com_post']


admin.site.register(Comments, CommentsAdmin)
