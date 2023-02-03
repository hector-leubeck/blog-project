from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone


class Post (models.Model):
    post_title = models.CharField(max_length=255, verbose_name='Título')
    post_author = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Escrito por')
    post_date = models.DateTimeField(
        default=timezone.now, verbose_name='Data de criação')
    post_content = models.TextField(verbose_name='Conteúdo')
    post_resume = models.TextField(
        verbose_name='Resumo', default='Digite o resumo da postagem.')
    post_category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, blank=True,
        null=True, verbose_name='Categoria')
    post_img = models.ImageField(
        upload_to='post_img/%Y/%m',
        blank=True, null=True, verbose_name='Imagem')
    post_pub = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.post_title
