from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .forms import UserCreateForm


def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupaccount.html', {'form': UserCreateForm,
                                                              'error': 'Użytkownik już istnieje, wprowadź inną nazwę'})
        else:
            return render(request, 'signupaccount.html', {'form': UserCreateForm,
                                                          'error': 'Hasła nie pasują do siebie'})

def logoutaccount(request):
    logout(request)
    return redirect('home')