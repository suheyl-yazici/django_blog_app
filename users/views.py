from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserProfileForm,UpdateUserForm,UserForm
from .models import Profile, User
from django.contrib.auth.decorators import login_required


@login_required
def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return render(request, 'user/logout.html')

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    
    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, 'login successfull')
            login(request, user)
            return redirect('home')
    return render(request, 'user/user_login.html',{"form": form})

def register(request):
    form_user = UserForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST, request.FILES)
        if form_user.is_valid():
            form_user.save()
            username = form_user.cleaned_data['username']
            password = form_user.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, 'Register Successfull')
            login(request, user)
            return redirect('home')
    context={
        'form_user': form_user,
    }
    return render(request, 'user/register.html', context)

@login_required
def profile(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST,request.FILES ,instance=request.user.profile)

        if profile_form.is_valid():
        
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('home')
    else:
    
        profile_form = UserProfileForm(instance=profile)

    context = {
        'profile_form': profile_form,

    }

    return render(request, 'user/profile.html', context)
