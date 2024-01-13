from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import PostForm

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

    return render(
        request,
        "forum/post_detail.html",
        {
        "post": post,
        "post_comments": post_comments,
        "comment_count": comment_count,
        "like_count": like_count,
        },
    )

def post_create(request):
    post_form = PostForm()

    return render(
        request,
        "forum/post_create.html",
        {
        "post_form": post_form,
        },
    )


