from django.shortcuts import render
from shop.models import Category, Carousel, Product, SoldProduct
import random
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from shop.forms import CreateUserForm
from django.contrib.auth.models import Group

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
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

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
            messages.success(request,'Account was Created For ' + username)
            return redirect('login')

    context = {'category':category,'form':form}
    return render(request,'Login.html',context)

def Logout(request):
    logout(request)
    return redirect('login')