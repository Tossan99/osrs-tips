from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

CATEGORY = (
    ("none", "None"), ("pvm", "PvM"), ("pvp", "PvP"), ("skilling", "Skilling"), ("questing", "Questing"))

class Post(models.Model):
    """
    Model for user posts
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts")
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.TextField(choices=CATEGORY, default="none")
    content = models.TextField(max_length=5000, blank=True)
    excerpt = models.TextField(max_length=150, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    post_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='forum_post_likes', blank=True)

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Written by {self.author}"

    def save(self, *args, **kwargs):
        if not self.slug:
            """
            Generate a unique slug based on the title and timestamp
            """
            base_slug = slugify(self.title)
            timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
            unique_slug = f"{base_slug}-{timestamp}"
            self.slug = unique_slug

        super().save(*args, **kwargs)

class Comment(models.Model):
    """
    Model for users comments
    """
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