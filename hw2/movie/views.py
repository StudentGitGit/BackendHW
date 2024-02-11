from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie

def get_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movies_list.html', {'movies': movies})

def get_movie_by_id(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})
