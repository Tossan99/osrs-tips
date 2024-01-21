from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
CATEGORY = (
    (0, "None"), (1, "PvM"), (2, "PvP"), (3, "Skilling"), (4, "Questing"))

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="forum_posts")
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    content = models.TextField(max_length=2000, blank=True)
    excerpt = models.TextField(max_length=200, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    post_image = CloudinaryField('image', default='placeholder')
    

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Written by {self.author}"

class Comment(models.Model):
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="post_commenter")
    post = models.ForeignKey(
    Post, on_delete=models.CASCADE, related_name="post_comments")
    content = models.TextField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.author}'s comment on {self.post}"

class Like(models.Model):
    liker = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="post_liker")
    post = models.ForeignKey(
    Post, on_delete=models.CASCADE, related_name="post_likes")
    like = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.liker} liked {self.post}"