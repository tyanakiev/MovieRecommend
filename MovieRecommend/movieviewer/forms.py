from .models import Movie
from django import forms


class MoviesSearch(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2'}))

