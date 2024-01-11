from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))
CATEGORY = (
    (0, "None"), (1, "PvM"), (2, "PvP"), (3, "Skilling"), (4, "Questing"))

class Post(models.Model):
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="forum_posts")
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    content = models.TextField(max_length=2000, blank=True)
    excerpt = models.TextField(max_length=200, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # post_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"