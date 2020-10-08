"""
フォーム
"""
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    """
    クラス
    """
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    """
    クラス
    """
    class Meta:
        model = Comment
        fields = ('author', 'text',)
