from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comments(models.Model):
    com_name = models.CharField(max_length=200, verbose_name='Nome')
    com_email = models.EmailField(verbose_name='Email')
    commentary = models.TextField(verbose_name='Comentário')
    com_post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                 verbose_name='Post')
    com_user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                 verbose_name='Autor')
    com_date = models.DateTimeField(default=timezone.now, verbose_name='Data')
    com_pub = models.BooleanField(default=True, verbose_name='Publicado')

    def __str__(self) -> str:
        return self.com_name
