from django import forms
from .models import Post
from .models import PostCategory


class PostCategoryForm(forms.ModelForm):
    class Meta:
        model = PostCategory
        fields = ['CategoryName']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title', 'Contents']
