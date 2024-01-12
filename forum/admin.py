from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status')
    search_fields = ['title']
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)