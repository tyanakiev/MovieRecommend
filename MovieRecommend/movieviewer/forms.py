from .models import Movie
from django import forms


class MoviesSearch(forms.Form):
    movie_title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm ml-3 w-75'}))

