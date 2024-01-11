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

    return render(
        request,
        "forum/post_detail.html",
        {
        "post": post,
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


