from django import forms
from django.forms import TextInput, FileInput
from movies.models import Movie, MovieRate


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date', 'image_file', 'image_link', 'rate',)
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

            'image_file': FileInput(
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


class SearchForm(forms.Form):
    text = forms.CharField(required=True)
    widgets = {
        'text': TextInput(
            attrs={
                'class': 'form-control me-2',
                'placeholder': 'Search IMDb',
                'type': 'text',
            },

        )
    }

