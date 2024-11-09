from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from forum import views as forum_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html', next_page='forum-home'), name='logout'),
    path('register/', forum_views.register, name='register'),
]