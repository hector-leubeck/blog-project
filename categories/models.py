from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name='Categoria')

    def __str__(self) -> str:
        return self.cat_name
