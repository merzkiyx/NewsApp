from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

class Post(models.Model):
    ARTICLE = "AR"
    NEWS = "NW"
    TYPE_CHOICES = [
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость'),
    ]
    name = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts')
    pub_date = models.DateTimeField(auto_now_add=True)
    post_type = models.CharField(max_length=2, choices=TYPE_CHOICES)

    def __str__(self):
        return f'{self.name.title()}: {self.content[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()