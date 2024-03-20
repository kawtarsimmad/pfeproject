from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def index(request):
    return render(request, 'app/inner-page.html')

def index(request):
    return render(request, 'app/portfolio-details.html')


