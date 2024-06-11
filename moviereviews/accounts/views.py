from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def signupaccount(request):
    return render(request, 'signupaccount.html', {'form': UserCreationForm})
