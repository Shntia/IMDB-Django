from django.shortcuts import render, redirect
from .forms import UserLogInForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate


def authentication(request):
    login_form = UserLogInForm()
    register_form = UserRegisterForm()
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            user = authenticate(request, username=request.POST.get('username'),
                                password=request.POST.get('password'))
            if user:
                login(request, user)
                return redirect('movies_list')
            else:
                messages.error(request, "Unsuccessful login. Invalid information.")
                return render(request, 'user/authentication.html',
                              context={'register_form': register_form, 'login_form': login_form})

        elif request.POST.get('submit') == 'sign_up':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('movies_list')
            else:
                return render(request, 'user/authentication.html',
                              context={'register_form': register_form, 'login_form': login_form})
    return render(request, 'user/authentication.html',
                  context={'register_form': register_form, 'login_form': login_form})

