# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, PostForm
from .models import Post, Profile
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            messages.error(request, 'Invalid username or password')
            
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def feed(request):
    # Show ALL posts from everyone
    posts = Post.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(request, 'feed.html', {'posts': posts, 'form': form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('feed')

@login_required
def profile(request, username):
    user_obj = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user_obj).order_by('-created_at')
    
    # Get or create profile
    profile, created = Profile.objects.get_or_create(user=user_obj)
    
    # Check if current user is following this profile's user
    # We check if user_obj is in request.user's following list
    # But our model uses 'followers' on the Profile, so we check that
    is_following = profile.followers.filter(id=request.user.id).exists()

    return render(request, 'profile.html', {'user_obj': user_obj, 'posts': posts, 'is_following': is_following})

@login_required
def follow_unfollow(request, username):
    # Get the profile of the user we want to follow/unfollow
    target_profile = get_object_or_404(Profile, user__username=username)
    current_user_profile, _ = Profile.objects.get_or_create(user=request.user)
    
    # If current user is already following, unfollow
    if target_profile.followers.filter(id=request.user.id).exists():
        target_profile.followers.remove(request.user)
    else:
        # Follow: Add current user to target's followers
        target_profile.followers.add(request.user)
        
    return redirect('profile', username=username)