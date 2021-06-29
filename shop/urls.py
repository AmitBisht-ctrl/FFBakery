from django.urls import path
from shop.views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('category/<str:cat>', category, name='category'),
    path('login/', Login, name='login'),
    path('signup/',SignUp, name='signup'),
    path('logout/',Logout, name='logout'),
    path('cart/',cart, name='cart'),
]
