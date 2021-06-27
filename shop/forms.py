from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

class CreateUserForm(UserCreationForm):
    # Username.widgets = {placeholder:}
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'autocomplete': 'new-password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'autocomplete': 'new-password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs = {'placeholder': "Username"}),
            'email': forms.EmailInput(attrs = {'placeholder': "Email Address"}),
        }