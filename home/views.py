from django.shortcuts import render

# Create your views here.

# index page view


def index(request):
    return render(request, 'home/index.html')
