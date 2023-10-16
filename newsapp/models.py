from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

class Post(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    author = models.CharField(
        max_length=100,
    )
    content = models.TextField()

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='post',
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name.title()}: {self.content[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()