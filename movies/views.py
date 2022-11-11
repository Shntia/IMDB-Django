from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from movies.models import Movie
from movies.forms import MovieForm

# def movie_view(request):
#     movie_list = Movie.objects.all()
#     context = {
#         'movies': movie_list
#     }
#     return render(request, 'movies/movies.html', context)


def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        context = {
            "movies": movies,
            "user": "Arash",
            "is_valid": True
        }
        return render(request, 'movies/movies_list.html', context=context)

    elif request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('movies_list')

        return movie_add(request, form)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'GET':
        return HttpResponse(f'<h1>This is movie {pk}</h1>')

    elif request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if not form.is_valid():
            return movie_edit(request, pk, movie_form=form)

        form.save()
        return redirect('movie_detail', pk=pk)


def movie_add(request, movie_form=None):
    if not movie_form:
        movie_form = MovieForm()
    return render(request, 'movies/movie_add.html', context={'form': movie_form})


def movie_edit(request, pk, movie_form=None):
    movie = get_object_or_404(Movie, pk=pk)

    if not movie_form:
        movie_form = MovieForm(instance=movie)

    context = {
        'form': movie_form,
        'movie': movie
    }
    return render(request, 'movies/movie_edit.html', context=context)


def movie_delete(request, pk):
    pass