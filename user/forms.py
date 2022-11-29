from django import forms
from .models import User
from django.forms import TextInput, EmailInput
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

        def clean_username(self):
            raise ValidationError(_('username is not correct'))

        def clean_password(self):
            raise ValidationError(_('password is not correct'))

        def clean_email(self):
            raise ValidationError(_('email is not correct'))

        def full_clean(self):
            raise ValidationError(_('email and username and password is not correct'))

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

        def clean_username(self):
            raise ValidationError(_('username is not correct'))

        def clean_password(self):
            raise ValidationError(_('password is not correct'))

        def full_clean(self):
            raise ValidationError(_('username and password is not correct'))

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
