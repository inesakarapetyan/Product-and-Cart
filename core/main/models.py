from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Product(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_prod', blank=True)
    img = models.ImageField('Product image', upload_to='product image', blank=True)
    name = models.TextField('Product name')
    price = models.PositiveIntegerField('Product price')
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Pay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    name = models.TextField('Name')
    card_number = models.PositiveIntegerField('Card number')
    hetevi_tver = models.PositiveIntegerField('Hetevi tver')
    phone_number = models.PositiveIntegerField('Phone number')
    email = models.EmailField('Email')

    def __str__(self):
        return self.name
    

class ContactUs(models.Model):
    name = models.CharField('Name', max_length=50)
    phone = models.CharField('Phone number', max_length=60)
    email = models.EmailField('Email')
    address = models.TextField('Address')
    message = models.TextField('Message')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name ='Contact Us'
        verbose_name_plural = 'Contact Us'



class UserMessage(models.Model):
    
    name = models.CharField('Name', max_length=50)
    phone = models.CharField('Phone number', max_length=60)
    email = models.EmailField('Email')
    address = models.TextField('Address')
    message = models.TextField('Message')

    def __str__(self):
        return self.name