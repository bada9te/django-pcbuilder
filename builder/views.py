from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import UserCreationForm, UserLoginForm, PcBuildForm
from .models import User, GPU, CPU, RAM, Motherboard, Storage, Box, PSU



# Create your views here.
def index(request):
    context = {}
    print("User:", request.user)

    return render(request, 'builder/index.html', context)

@login_required(login_url='sign-in')
def setup(request):
    # handle post (save user's pc build)
    if request.method == 'POST':
        form = PcBuildForm(request.POST)
        if form.is_valid():
            pcBuild = form.save(commit=False)
            pcBuild.user = request.user
            pcBuild.save()
            return redirect('index')
        
    # return page on GET request
    form = PcBuildForm()
    context = {
        "form": form,
    }
    return render(request, 'builder/setup.html', context)


def login_user(request):
    if request.user is not None and request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        if user is None:
            messages.error(request, 'User with this email does not exist')
            return redirect('sign-in')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('sign-in')

    # process GET request
    form = UserLoginForm()
    context = {
        "page": "login",
        "form": form
    }
    return render(request, 'builder/login-register.html', context)


def register_user(request):
    if request.user is not None and request.user.is_authenticated:
        return redirect('index')

    # handle form submission
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user = User.objects.create_user(email=email, password=password, username=username)
            login(request, user)
            return redirect('index')

    # process default GET request
    form = UserCreationForm()
    context = {
        "page": "register",
        "form": form
    }
    return render(request, 'builder/login-register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index', permanent=True)