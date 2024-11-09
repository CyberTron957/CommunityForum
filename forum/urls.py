from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='forum-home'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
]