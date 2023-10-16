from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms



class PostFilter(FilterSet):
    min_pub_date = DateFilter(
        widget=forms.TextInput(attrs={'type': 'date'}),
        field_name='pub_date'
    )

    class Meta:
        model = Post
        fields = {
            'name': ['icontains'],
            'author': ['exact'],
        }