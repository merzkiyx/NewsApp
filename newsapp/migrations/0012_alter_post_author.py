# Generated by Django 4.2.5 on 2023-10-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0011_remove_post_quantity_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]