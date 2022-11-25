from django.shortcuts import render, redirect
from .forms import UserLogInForm, UserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.cache import *
from django.http import HttpResponseRedirect


def login_view(request):
    if request.user.is_anonymous:
        if request.method == "GET":
            form = UserLogInForm()
            return render(request, 'registration/login.html', context={'form': form})
        elif request.method == "POST":
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                login(request, user)
                return redirect('movies_list')
            else:
                form = UserLogInForm()
                return render(request, 'registration/login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('movies_list')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful.")
            login(request, user)
            return redirect('movies_list')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserForm()
    return render(request, 'registration/login.html', context={'form': form})
