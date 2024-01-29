from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Post, Comment
from .forms import PostForm, CommentForm

def redirect_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif not request.user.is_authenticated:
        return redirect('about')
    

# Home page
#--------------------------------------------------
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "forum/index.html"


# Category pages
#--------------------------------------------------
class PvmList(generic.ListView):
    queryset = Post.objects.filter(category=1)
    template_name = "forum/category_pvm.html"


class PvpList(generic.ListView):
    queryset = Post.objects.filter(category=2)
    template_name = "forum/category_pvp.html"


class SkillingList(generic.ListView):
    queryset = Post.objects.filter(category=3)
    template_name = "forum/category_skilling.html"

class QuestingList(generic.ListView):
    queryset = Post.objects.filter(category=4)
    template_name = "forum/category_questing.html"


# About page
#--------------------------------------------------
def about_page(request):
    return render(request, "forum/about.html")


# Posts
#--------------------------------------------------
def post_detail(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    post_comments = post.post_comments.all().order_by("-created_on")
    comment_count = post.post_comments.filter(approved=True).count()
    post_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post_liked = True

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
            "post_liked": post_liked,
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
                "category": request.POST["category"],
                "content": request.POST["content"],
                "excerpt": request.POST["excerpt"],
                "post_image": request.FILES["post_image"],
            },
        )
        messages.add_message(request, messages.SUCCESS, 'Post updated successfully')
        return redirect("home")

def post_delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS,'Post deleted successfully!')
    else:
        messages.add_message(request, messages.ERROR, 'Error deleting post')
    
    return redirect("home")

# Comments
#--------------------------------------------------
def comment_edit(request, slug, comment_id):
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
            messages.add_message(request, messages.SUCCESS, 'Comment updated successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
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

# Likes
#--------------------------------------------------
class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

