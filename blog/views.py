"""
ビュー
"""
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

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

@login_required
def post_new(request):
    """
    記事作成フォーム作成
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', _pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, _pk):
    """
    記事登録・更新フォーム作成
    """
    post = get_object_or_404(Post, pk=_pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', _pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    """
    下書き一覧フォーム作成
    """
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, _pk):
    """
    公開フォーム作成
    """
    post = get_object_or_404(Post, pk=_pk)
    post.publish()
    return redirect('post_detail', pk=_pk)


@login_required
def post_remove(request, _pk):
    """
    削除フォーム作成
    """
    post = get_object_or_404(Post, pk=_pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, _pk):
    """
    コメント投稿
    """
    post = get_object_or_404(Post, pk=_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', _pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, _pk):
    """
    コメント承認
    """
    comment = get_object_or_404(Comment, pk=_pk)
    comment.approve()
    return redirect('post_detail', _pk=comment.post.pk)

@login_required
def comment_remove(request, _pk):
    """
    コメント却下
    """
    comment = get_object_or_404(Comment, pk=_pk)
    comment.delete()
    return redirect('post_detail', _pk=comment.post.pk)
