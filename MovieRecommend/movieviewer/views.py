from django.shortcuts import render

from .forms import MoviesSearch
from .models import Movie
from django.core.paginator import Paginator


def index(request):

    if request.method == 'POST':
        form = MoviesSearch(request.POST)
        if form.is_valid():
            movies_data = Movie.objects.all().filter(title__contains=form.cleaned_data['title']).order_by('-avg_vote')
            paginator = Paginator(movies_data, 28)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'movieviewer/index.html', {'movies': page_obj, 'form': form})

    else:
        form = MoviesSearch()
        movies_data = Movie.objects.all().order_by('-avg_vote')
        paginator = Paginator(movies_data, 28)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'movieviewer/index.html', {'movies': page_obj, 'form': form})

