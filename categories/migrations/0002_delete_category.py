# Generated by Django 4.1.5 on 2023-01-27 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_delete_post'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]