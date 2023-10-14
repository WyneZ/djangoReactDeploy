from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def home(request):

    context = {'data': 'This data is from django'}
    return render(request, 'home.html', context)