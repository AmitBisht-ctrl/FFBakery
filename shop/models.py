from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# from django.core.validators import RegexValidator

# Create your models here.

# EMAIL_VALIDATOR = RegexValidator()
# PHONE_NUMBER_REGEX = RegexValidator(r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$', 'Please provide a valid phone number')

class Category(models.Model):
    sno = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    Image = models.ImageField()

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
    LightBackgroundColor = models.CharField(max_length=50)
    DarkBackgroundColor = models.CharField(max_length=50)
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
        return (self.product.ProductName + ' - Sold to - ' + self.user.username)
    
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

    def __str__(self):
        return self.User + ' ' + self.product

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40,null=True,blank=True)
    email = models.EmailField(max_length=250)
    phone_no = models.CharField(max_length=10)
    query = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.query
