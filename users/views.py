from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password != password2:
            return render(request, "users/register.html", {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, "users/register.html", {"error": "Username already exists"})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        return redirect("/")

    return render(request, "users/register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        return render(request, "users/login.html", {"error": "Invalid username or password"})

    return render(request, "users/login.html")


def user_logout(request):
    logout(request)
    return redirect("/")
