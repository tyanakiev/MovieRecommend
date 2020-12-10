from django.shortcuts import render

from .forms import MoviesSearch
from .models import Movie
from django.core.paginator import Paginator


def index(request):

    if request.method == 'POST':
        form = MoviesSearch(request.POST)
        if form.is_valid():
            if form.cleaned_data['title']:
                movies_data = Movie.objects.all().filter(rating__isnull=False, primaryTitle__icontains=form.cleaned_data['title'],
                                                         titleType='movie', ).order_by("-rating__averageRating")
            else:
                movies_data = Movie.objects.all().filter(rating__isnull=False, titleType='movie').order_by("-rating__averageRating")

            paginator = Paginator(movies_data, 52)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'movieviewer/index.html', {'movies': page_obj, 'form': form})

    else:
        form = MoviesSearch()
        movies_data = Movie.objects.all().filter(rating__isnull=False, titleType='movie').order_by("-rating__averageRating")
        paginator = Paginator(movies_data, 52)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'movieviewer/index.html', {'movies': page_obj, 'form': form})

