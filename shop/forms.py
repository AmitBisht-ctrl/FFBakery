from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import fields, widgets
# from django.forms import widgets
from shop.models import Contact
from django.core import validators

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

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        validators=[
            validators.MaxLengthValidator(40,'First name cannot be more than 40 letters'),
            validators.MinLengthValidator(3,'First Name must be greater than 3 letter')
        ])
    last_name = forms.CharField(
        validators=[
            validators.MaxLengthValidator(40,'Last name cannot be more than 40 letters'),
            validators.MinLengthValidator(3,'Last Name must be greater than 3')
        ])

    phone_no = forms.CharField(widget = forms.NumberInput(attrs={'max_length':10}),
    validators=[
        validators.MinLengthValidator(10)
    ])

    email = forms.CharField(
        validators=[
            validators.EmailValidator
        ])

    query = forms.CharField(widget=forms.TextInput(attrs={'cols':30, 'rows':2}),
        validators = [validators.MinLengthValidator(5, 'You have to write something inorder to contact.')]
    )

    class Meta:
        model = Contact
        fields = '__all__'
