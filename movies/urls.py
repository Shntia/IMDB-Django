from django.urls import path

from .views import movies_list, movie_detail, movie_add, movie_edit


urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('movie/', movie_detail, name='movie.det'),
    path('<int:pk>/edit/', movie_edit, name='movie_edit'),
    path('add/', movie_add, name='movie_add'),

]