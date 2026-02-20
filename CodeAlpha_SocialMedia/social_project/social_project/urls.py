# social_project/urls.py
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.feed, name='feed'), # Redirects to feed, which requires login
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/follow/', views.follow_unfollow, name='follow_unfollow'),
]