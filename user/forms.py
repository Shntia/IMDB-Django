from django import forms
from .models import User
from django.forms import TextInput, EmailInput


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': "Username",
                    'type': "text",
                    'class': "input"
                },
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': "Email",
                    'type': "email",
                    'class': "input"
                },
            ),
            'password': TextInput(
                attrs={
                    'placeholder': "Password",
                    'type': "password",
                    'class': "input"
                },
            )
        }


class UserLogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': "Username",
                    'type': "text",
                    'class': "input"
                },

            ),
            'password': TextInput(
                attrs={
                    'placeholder': "Password",
                    'type': "Password",
                    'class': "input"
                },
            )
        }
