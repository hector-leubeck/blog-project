# Generated by Django 4.1.5 on 2023-02-03 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0005_comments_com_pub'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='com_email',
            field=models.EmailField(default='nome@email.com', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='com_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]
