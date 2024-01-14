from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "forum/index.html"

def post_detail(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    post_comments = post.post_comments.all().order_by("-created_on")
    comment_count = post.post_comments.filter(approved=True).count()
    like_count = post.post_likes.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval!'
    )
    
    comment_form = CommentForm()

    return render(
        request,
        "forum/post_detail.html",
        {
            "post": post,
            "post_comments": post_comments,
            "comment_count": comment_count,
            "like_count": like_count,
            "comment_form": comment_form,
        },
    )

def post_create(request):
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Post submitted and awaiting approval!')
            
    post_form = PostForm()
            
    return render(
        request,
        "forum/post_create.html",
        {
            "post_form": post_form,
        },
    )


