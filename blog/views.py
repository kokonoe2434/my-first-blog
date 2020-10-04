"""
ビュー
"""
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    """
    記事リストのトップ作成
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, _pk):
    """
    記事本体作成
    """
    post = get_object_or_404(Post, pk=_pk)
    return render(request, 'blog/post_detail.html', {'post': post})
