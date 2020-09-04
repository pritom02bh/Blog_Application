from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UsercreationFrom


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
