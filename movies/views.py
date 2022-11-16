from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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


def movie_detail(request, name):
    movies = Movie.objects.get(title=name)
    context = {
        'name': movies.title,
        'date': movies.release_date.year,
        'image': movies.image_link,
        'description': movies.description,
        'rate': movies.rate,
        'genrs': movies.genres.all().values('title'),
    }
    return render(request, "movies/movie_detail.html", context=context)
