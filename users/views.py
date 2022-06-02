from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import UserForm, UserProfileForm
from django.contrib import messages


def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        if user:
            login(request, user)
        return redirect('home')

    return render(request, 'user/user_login.html', {'form': form})

def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST)
        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            messages.succes(request, 'Register successfully')
        return redirect('home')

    context= {
        'form_user': form_user,
        'form_profile': form_profile,
    }
    return render(request, 'user/register.html', context)

def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return render(request, 'user/logout.html')
