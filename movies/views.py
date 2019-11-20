from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre, Review

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies,}
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, 'movies/index.html')
    