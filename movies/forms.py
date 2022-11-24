from django import forms
from django.forms import TextInput
from movies.models import Movie, MovieRate


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date', 'image_link', 'rate')
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 1%; margin-bottom: 5%'
                },

            ),
            'rate': TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 1%; margin-bottom: 5%'

                }
            ),
            'release_date': TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 1%; margin-bottom: 5%'
                },

            ),
            'image_link': TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 1%; margin-bottom: 5%'
                },

            ),
            'description': TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 1%; margin-bottom: 5%'
                },

            ),
        }


class RateForm(forms.ModelForm):
    class Meta:
        model = MovieRate
        fields = ('rate',)
