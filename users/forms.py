from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile ,User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2',)


class UserProfileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))
    class Meta:
        model = UserProfile
        fields = ('image', 'bio',)


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email',)
