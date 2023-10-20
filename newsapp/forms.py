from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'name',
            'content',
            'author',
            'category',
            'post_type'
        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        content = cleaned_data.get("content")

        if name == content:
            raise ValidationError(
                "Содержание не должно быть идентичным названию."
            )

        return cleaned_data


