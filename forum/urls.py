from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_create/', views.post_create, name='post_create'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]