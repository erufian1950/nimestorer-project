from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products': products})

def contact(request):
    return render(request, 'contact.html')

def gallery(request):   
    return render(request, 'gallery.html')

def support(request):
    return render(request, 'support.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')