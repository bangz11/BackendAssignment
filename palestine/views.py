from django.shortcuts import render

def home(request):
    return render(request, "palestine/index.html")