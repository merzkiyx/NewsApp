# Generated by Django 4.2.5 on 2023-10-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]