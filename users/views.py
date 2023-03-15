from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegisterForm


def log_out(request):
    logout(request)
    return redirect('recipes:index')


def register(request):
    # GET request for rendering the page.
    if request.method != 'POST':
        form = RegisterForm()
    # POST request for creating a new user.
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
