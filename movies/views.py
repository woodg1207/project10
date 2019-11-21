from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies,}
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    reviewform = ReviewForm()
    context = {'movie':movie, 'reviews':reviews, 'reviewform':reviewform,}
    return render(request, 'movies/detail.html',context)

@require_POST
def review_create(request, movie_pk):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                new = form.save(commit=False)
                new.movie_id = movie_pk
                new.user = request.user
                new.save()
                return redirect('movies:detail', movie_pk)
    return redirect('movies:index')

@login_required
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('movies:detail', movie_pk)

@login_required
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:index')

@login_required
def follow(request, movie_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
        else:
            person.followers.add(user)
    return redirect('movies:detail', movie_pk)