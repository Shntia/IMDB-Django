from django.shortcuts import render, redirect, get_object_or_404

from comment.models import AbstractComment
from movies.models import Movie, MovieComment, MovieRate
from movies.forms import MovieForm, RateForm
from comment.forms import CommentForm


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
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)

    if not movie_form:
        movie_form = MovieForm(instance=movie)

    context = {
        'form': movie_form,
        'movie': movie
    }
    return render(request, 'movies/movie_edit.html', context=context)


def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)
    movie.is_valid = False
    movie.save()
    return redirect('movies_list')


def movie_detail(request, name):
    movie = Movie.objects.get(title=name)
    comment = MovieComment.objects.filter(movie=movie, status=AbstractComment.APPROVED)
    new_comment = None
    if request.method == 'POST':
        if request.POST.get('rate'):
            if request.user.is_authenticated:
                rate_form = RateForm(request.POST)
                if rate_form.is_valid():
                    MovieRate.objects.update_or_create(user=request.user,
                                                       movie=movie,
                                                       defaults={'rate': int(request.POST.get('rate'))}
                                                       )
                    return redirect('.')
                else:
                    return redirect('login')

        if request.POST.get('comment'):
            if request.user.is_authenticated:
                comment_form = CommentForm(data=request.POST)
                if comment_form.is_valid():
                    MovieComment.objects.create(
                        user=request.user,
                        movie=movie,
                        comment_body=request.POST.get("comment_body")
                    )
                    return redirect('.')
            else:
                return redirect('login')
    else:
        rate_form = RateForm()
        comment_form = CommentForm()

    context = {
        'name': movie.title,
        'date': movie.release_date.year,
        'image': movie.image_link,
        'description': movie.description,
        'rate': movie.rate,
        'genrs': movie.genres.all().values('title'),
        'comments': comment,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'rate_form': rate_form,
    }
    return render(request, "movies/movie_detail.html", context=context)

