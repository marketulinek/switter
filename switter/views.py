from django.shortcuts import render, redirect
from .forms import SweetForm
from .models import Profile, Sweet


def dashboard(request):
    followed_sweets = Sweet.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by('-created_at')
    form = SweetForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            sweet = form.save(commit=False)
            sweet.user = request.user
            sweet.save()
            return redirect('switter:dashboard')

    return render(request, 'switter/dashboard.html', {'form': form, 'sweets': followed_sweets})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
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