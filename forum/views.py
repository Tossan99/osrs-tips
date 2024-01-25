from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
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
            messages.add_message(request, messages.SUCCESS, 'Comment submitted and awaiting approval!')
    
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
    post_form = PostForm()
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Post submitted and awaiting approval')
            return redirect("home")
      
    return render(
        request,
        "forum/post_create.html",
        {
            "post_form": post_form,
        },
    )

def post_edit(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(pk=post_id)
        return render(
            request,
             "forum/post_edit.html",
            {
                "post": post
            },
        )
    elif request.method == "POST":
        post = Post.objects.update_or_create(
            pk=post_id,
            defaults={
                "title": request.POST["title"],
                "content": request.POST["content"],
                "excerpt": request.POST["excerpt"],
                "post_image": request.FILES["post_image"],
            },
        )
        messages.add_message(request, messages.SUCCESS, 'Post updated successfully')
        return redirect("home")

def post_delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    messages.add_message(
                request, messages.SUCCESS,
        'Post deleted!'
    )
    return redirect("home")


def comment_edit(request, slug, comment_id):
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted successfully')
    else:
        messages.add_message(request, messages.ERROR, 'Error deleting comment')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

