from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SweetForm
from .models import Profile, Sweet
from .utils import *
from decouple import config


def dashboard(request):

    if request.user.is_authenticated:
        followed_sweets = Sweet.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by('-created_at')

        form = SweetForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                sweet = form.save(commit=False)
                sweet.user = request.user
                sweet.content = translate_into_snake_hiss(request.POST.get('content'))
                sweet.save()
                return redirect('switter:dashboard')
    else:
        followed_sweets = Sweet.objects.all().order_by('-created_at')
        form = None

    return render(request, 'switter/dashboard.html', {'form': form, 'sweets': followed_sweets})

def profile_list(request):
    
    profiles = Profile.objects.all()

    return render(request, 'switter/profile_list.html', {'profiles': profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)

    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(profile)
        if action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, 'switter/profile.html', {'profile': profile})

def login_as(request):

    # In case the user is already logged in
    if request.user.is_authenticated:
        return redirect('switter:dashboard')

    random_user = User.objects.exclude(username='serpent').order_by('?').first()

    if request.method == 'POST':
        user = authenticate(request,username=request.POST.get('username'), password=config('SSSS'))
        if user:
            login(request, user)
        # TODO: in case the password is wrong
        return redirect('switter:dashboard')

    return render(request, 'registration/login_as.html', {'random_username': random_user.username})