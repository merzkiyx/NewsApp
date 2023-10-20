from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms



class PostFilter(FilterSet):
    min_pub_date = DateFilter(
        widget=forms.DateInput(attrs={'type': 'date'}),
        field_name='pub_date',
        lookup_expr='date__gte'
    )

    class Meta:
        model = Post
        fields = {
            'name': ['icontains'],
            'author': ['exact'],
        }