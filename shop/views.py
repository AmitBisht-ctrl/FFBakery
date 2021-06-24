from django.shortcuts import render
from shop.models import *

# Create your views here.
def home(request):
    category = Category.objects.all()
    carousel = Carousel.objects.all().first()
    
    context = {'category': category, 'carousel':carousel}
    return render(request, 'home.html',context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def category(request):
    return render(request, 'category.html')

def Login(request):
    return render(request, 'Login.html')