from django.shortcuts import render
from .models import Movie
from django.core.paginator import Paginator


def index(request):
    movies_data = Movie.objects.all().order_by('-avg_vote').filter(reviews_from_users__gt=1000)
    paginator = Paginator(movies_data, 28)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'movieviewer/index.html', {'movies': page_obj})
