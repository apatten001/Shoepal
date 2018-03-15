from django.shortcuts import render
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout
)
from .forms import UserLoginForm

# Create your views here.


def login_view(request):
    template_name = 'accounts/login.html'
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

    return render(request, template_name , {'form': form, 'title':title})


def logout_view(request):
    return render(request, 'home.html', {})

def register_view(request):
    return render(request, 'home.html', {})
