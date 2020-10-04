"""
フォーム
"""
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """
    クラス
    """
    class Meta:
        model = Post
        fields = ('title', 'text',)
