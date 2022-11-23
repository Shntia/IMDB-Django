from django import forms
from movies.models import MovieComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('comment_body',)
