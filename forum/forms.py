from .models import Post, Comment
from django import forms
from django_summernote.admin import SummernoteModelAdmin


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'excerpt', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)