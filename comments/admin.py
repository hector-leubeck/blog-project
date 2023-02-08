from django.contrib import admin
from .models import Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'com_name', 'com_post', 'com_date', 'com_pub')
    list_display_links = ['com_name', 'com_post']
    list_editable = ['com_pub']


admin.site.register(Comments, CommentsAdmin)
