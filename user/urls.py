from django.urls import path
from .views import authentication
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', authentication, name='authentication'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
