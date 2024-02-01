from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm


def redirect_view(request):
    """
    Redirects users that aren't loged in to the about page
    """
    if request.user.is_authenticated:
        return redirect('home')
    elif not request.user.is_authenticated:
        return redirect('about')


#
# Home page
#--------------------------------------------------
class PostList(generic.ListView):
    """
    View for displaying all posts
    """
    queryset = Post.objects.all()
    template_name = "forum/index.html"


#
# Category pages
#--------------------------------------------------
class PvmList(generic.ListView):
    """
    View for displaying PvM posts
    """
    queryset = Post.objects.filter(category="pvm")
    template_name = "forum/category_pvm.html"


class PvpList(generic.ListView):
    """
    View for displaying PvP posts
    """
    queryset = Post.objects.filter(category="pvp")
    template_name = "forum/category_pvp.html"


class SkillingList(generic.ListView):
    """
    View for displaying Skilling posts
    """
    queryset = Post.objects.filter(category="skilling")
    template_name = "forum/category_skilling.html"


class QuestingList(generic.ListView):
    """
    View for displaying Questing posts
    """
    queryset = Post.objects.filter(category="questing")
    template_name = "forum/category_questing.html"


#
# About page
#--------------------------------------------------
def about_page(request):
    """
    View for displaying the about page
    """
    return render(request, "forum/about.html")


#
# Posts
#--------------------------------------------------
def post_detail(request, slug):
    """
    View for displaying a posts details
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    post_comments = post.post_comments.all().order_by("-created_on")
    comment_count = post.post_comments.filter(approved=True).count()
    post_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post_liked = True

    if request.method == "POST":
        """
        Comment form
        """
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment submitted and awaiting approval')
        else:
            messages.add_message(request, messages.ERROR, 'Error submitting comment')

    comment_form = CommentForm()

    return render(
        request,
        "forum/post_detail.html",
        {
            "post": post,
            "post_comments": post_comments,
            "comment_count": comment_count,
            "post_liked": post_liked,
            "comment_form": comment_form,
        },
    )


def post_create(request):
    """
    View for creating posts
    """
    post_form = PostForm()
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid() and request.user.is_authenticated:
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Post submitted and awaiting approval')
            return redirect("home")
        else:
            messages.add_message(request, messages.ERROR, 'Error submitting post')

    return render(
        request,
        "forum/post_create.html",
        {
            "post_form": post_form,
        },
    )


def post_edit(request, post_id):
    """
    View for displaying edit post
    """
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid() and post.author == request.user:
            post_form.save()
            messages.add_message(request, messages.SUCCESS, 'Post edited and awaiting approval')
            return redirect("home")
        else:
            messages.add_message(request, messages.ERROR, 'Error editing post')

    else:
        post_form = PostForm(instance=post)

    return render(request, "forum/post_edit.html", {"post_form": post_form, })


def post_delete(request, post_id):
    """
    View to delete post
    """
    post = Post.objects.get(pk=post_id)
    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted successfully')
    else:
        messages.add_message(request, messages.ERROR, 'Error deleting post')

    return redirect("home")


#
# Comments
#--------------------------------------------------
def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment edited and awaiting approval')
        else:
            messages.add_message(request, messages.ERROR, 'Error editing comment')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comments
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted successfully')
    else:
        messages.add_message(request, messages.ERROR, 'Error deleting comment')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


#
# Likes
#--------------------------------------------------
class PostLike(View):
    """
    View to like posts
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if request.user.is_authenticated:
            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)

            return HttpResponseRedirect(reverse('post_detail', args=[slug]))


#
# Error
#--------------------------------------------------
def error_404(request, exception):
    """
    Redirects users to error 404 page if the url is invalid
    """
    return render(request, "404.html", status=404)
