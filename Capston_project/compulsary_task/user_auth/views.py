from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

# Create your views here.


def user_login(request):
    # shows the login screen
    return render(request, 'authentication/login.html')


def authenticate_user(request):
    # calls the username and password entered
    username = request.POST['username']
    password = request.POST['password']
    # checks if it is in the database and logs them in
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('polls:index')
        )

def register_user(request):
    if request.method == 'POST':
        # posts the inputs to the form and the database
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # saves changes
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, "Registration successful")
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(
                reverse('polls:index')
            )
        else:
            messages.error(request, "unsuccessful registration")
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'authentication/register_user.html', context)
