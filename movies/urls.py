from django.urls import path
from django.contrib.auth import views as auth_views
from .views import movies_list, movie_detail, movie_add, movie_edit, register


urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('movie/<str:name>/', movie_detail, name='movie_detail'),
    path('<int:pk>/edit/', movie_edit, name='movie_edit'),
    path('add/', movie_add, name='movie_add'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]
