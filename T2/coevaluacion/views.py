from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def ficha_coev(request):
    return render(request, 'ficha-coev.html')


def course(request):
    return render(request, 'course.html')

