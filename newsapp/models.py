from django.db import models
from django.core.validators import MinValueValidator

class Post(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    content = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='post',
    )

    def __str__(self):
        return f'{self.name.title()}: {self.content[:20]}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()