from django.urls import path
from shop.views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('category/', category, name='category'),
    path('login/', Login, name='Login'),
]
