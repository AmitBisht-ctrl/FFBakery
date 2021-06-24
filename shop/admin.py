from django.contrib import admin
from shop.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Carousel)
admin.site.register(Product)
admin.site.register(SoldProduct)
admin.site.register(Like)
admin.site.register(Comment)