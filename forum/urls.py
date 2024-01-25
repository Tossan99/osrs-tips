from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('pvm/', views.PvmList.as_view(), name='pvm'),
    path('pvp/', views.PvpList.as_view(), name='pvp'),
    path('questing/', views.QuestingList.as_view(), name='questing'),
    path('skilling/', views.SkillingList.as_view(), name='skilling'),
    path('about/', views.about_page, name='about'),
    path('post_create/', views.post_create, name='post_create'),
    path('post_edit/<int:post_id>', views.post_edit, name='post_edit'),
    path('post_delete/<int:post_id>', views.post_delete, name='post_delete'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]