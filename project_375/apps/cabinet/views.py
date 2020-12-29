from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'templates/base.html')

def privacy(request):
    return render(request, 'templates/privacy.html')
