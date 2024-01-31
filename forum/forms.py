from .models import Post, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "post_image",
            "title",
            "category",
            "content",
            "excerpt",
        ]
        widgets = {
            "content": SummernoteWidget(
                attrs={"class": "form-control",
                       "required": "required"}),
            "title": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Max 50 characters",
                       "required": "required"}),
            "excerpt": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Max 150 characters",
                       "required": "required"}),
            "category": forms.Select(
                attrs={"class": "form-control",
                       "required": "required"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]

        widgets = {
            "content": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Max 500 characters",}),
        }