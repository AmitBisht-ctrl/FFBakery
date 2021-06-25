from django.shortcuts import render
from shop.models import *
import random

# Create your views here.
def home(request):
    category = Category.objects.all()
    carouselList = Carousel.objects.all()

    carouselIndex = random.sample(range(0,len(carouselList)), k=4)

    carousels = [carouselList[idx] for idx in carouselIndex]

    print(carousels)
    
    context = {'category': category, 'carousels':carousels}
    return render(request, 'home.html',context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def category(request):
    return render(request, 'category.html')

def Login(request):
    return render(request, 'Login.html')