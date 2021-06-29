from django.conf.urls import url
from django.shortcuts import render
from shop.models import Category, Carousel, Product, SoldProduct
import random
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from shop.forms import CreateUserForm, ContactForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shop.decorators import login_must

# Create your views here.
def home(request):
    category = Category.objects.all()
    carouselList = Carousel.objects.all()

    carouselIndex = random.sample(range(0,len(carouselList)), k=4)

    carousels = [carouselList[idx] for idx in carouselIndex]
    dispProd = random.sample(carousels, k=2)

    allSoldProd = SoldProduct.objects.all()
    bestSeller = []
    for sp in allSoldProd:
        present = False
        for i in range(0,len(bestSeller)):
            if sp.product in bestSeller[i]:
                present = True
                bestSeller[i][0] += 1
                break

        if present == False:
            bestSeller.append([1,sp.product,sp.product])

    bestSeller.sort(reverse=True)
    bestSeller = [bs[1] for bs in bestSeller]

    context = {'category': category, 'carousels':carousels, 'bestsellers':bestSeller[:4], 'dispProd':dispProd}
    return render(request, 'home.html',context)

def contact(request):
    form = ContactForm()
    category = Category.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form, 'category':category}
    return render(request, 'contact.html', context)

def about(request):
    category = Category.objects.all()

    context = {'category': category}
    return render(request, 'about.html',context)

def category(request):
    return render(request, 'category.html')

def Login(request):
    category = Category.objects.all()
    form = CreateUserForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,f'<span>Welcome, {username.capitalize()}!</span> to FFBakery.')
            return redirect('home')
    
    context = {'category':category,'form':form}
    return render(request, 'Login.html',context)

def SignUp(request):
    category = Category.objects.all()
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account has been Created For <span>{username}</span>')
            return redirect('login')

    context = {'category':category,'form':form}
    return render(request,'Login.html',context)

def Logout(request):
    logout(request)
    return redirect('login')

@login_must
def cart(request):
    return render(request, 'cart.html')