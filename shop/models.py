from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    sno = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category
    

class Product(models.Model):
    sno = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=100,default='')
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    price = models.IntegerField(default=0)
    date_time = models.DateTimeField(default=now())
    ProductImage = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.ProductName

class Carousel(models.Model):
    sno = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    DisplayName = models.CharField(max_length=15)
    BackgroundColor = models.CharField(max_length=50)
    TransparentImage = models.ImageField()

    def __str__(self):
        return self.DisplayName
    

class SoldProduct(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    price = models.IntegerField(default=0)
    delivered = models.BooleanField(default=False)
    deliveryTime = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return (self.product + ' ' + self.user)
    
class Like(models.Model):
    sno = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('product','user')

class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_time = models.DateTimeField(default=now())


