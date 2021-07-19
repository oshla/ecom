""" from typing_extensions import Required """
from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager, Group
import os
import pdb
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
now = timezone.now()
# Create your models here.

class Customer(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True )
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, default='me@me.com', unique=True)
    address = models.CharField(null=True, blank=True, max_length=300)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    marital_status = models.CharField(max_length=50, null=True, blank=True)
    sc_handle = models.CharField(max_length=100, null=True, blank=True, unique=False, default='man')
    edu_qualification = models.CharField(max_length=50, null=True, blank=True)
    occupation = models.CharField(max_length=50, null=True, blank=True)
   
    state_of_origin = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.first_name


class Product(models.Model):
    name = models.CharField(null=True, max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    #price= models.FloatField()
    #digital field is kinda optional tho. determines if we need to ship a product or not based on if it is physical or not.
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=30, null=True, blank=True)


    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url= self.image.url
        except:
            url= ''
        return url

class Order(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    #complete is just like a condition like if its false that means we can add more products to our cart. basically we haven't confirmed if its all we want. sho get?
    complete = models.BooleanField(default=False, null=True, blank=False)
    Transaction_id = models.CharField(null=True, blank=True, max_length=100)
    username = models.CharField(null=True, blank=True, max_length=100)



    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping=False
        orderitems = self.order_item_set.all()
        for i in orderitems:
            if i.Product.digital == False:
                shipping=True
        return shipping

    @property
    def get_cart_total(self):
        orderitems= self.order_item_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems= self.order_item_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
        #this function basically calculates the quantity total and cost total. i mean they still have to be called tho

class Order_Item(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    Order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        print(self.quantity)
        total= self.Product.price * self.quantity
        return total


    #def __str__(self):
       # pass

class Shipping_Address(models.Model):
   Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
   Order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
   address = models.CharField(null=True, max_length=100)
   city = models.CharField(null=True, max_length=100)
   state = models.CharField(null=True, max_length=100)
   country = models.CharField(null=True, max_length=100)
   zipcode = models.CharField(null=True, max_length=100)

   def __str__(self):
       return str(self.address)

""" class MoreUserInfo(models.Model):
    First_name = models.CharField(max_length=50, null=True, blank=True)
    Last_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.ForeignKey('Age', models.SET_NULL, null=True, blank=True)
    gender = models.ForeignKey('Gender', models.SET_NULL, null=True, blank=True)
    email = models.EmailField(null=False, blank=False,default='me@me.com', unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    marital_status = models.ForeignKey('Status', models.SET_NULL, null=True, blank=True)
    sc_handle = models.CharField(max_length=100, null=True, blank=True)
    edu_qualification = models.ForeignKey('Education',  models.DO_NOTHING, null=False, blank=False)
    occupation = models.CharField(max_length=50, null=True, blank=True)
    income= models.FloatField()
    organization= models.CharField(max_length=100, null=True, blank=True)
    livestock = models.ForeignKey('Livestock', models.SET_NULL, null=True, blank=True)
    state_of_origin = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'

    def __str__(self):
        return self.First_name
 """

""" class Age(models.Model):
    name = models.CharField(max_length=9, blank=False, null=False)

    class Meta:
        verbose_name = 'Age'
        verbose_name_plural = 'Ages'

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=15, blank=False, null=False)

    class Meta:
        verbose_name = 'Sex'
        verbose_name_plural = 'Sex'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = 'Qualification'
        verbose_name_plural = 'Qualifications'

    def __str__(self):
        return self.name """




""" class States(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name """
    
class sampledata(models.Model):
    source = models.CharField(max_length=100, null=True, blank=True)
    Spath = models.IntegerField(_(""), null=True)
    edgeW = models.IntegerField(_(""), null=True)
    noOfEdges = models.IntegerField(_(""), null=True)
    from_handle = models.CharField(max_length=100, null=True, blank=True)
    to_handle = models.CharField(max_length=100, null=True, blank=True)
    dist = models.FloatField(_(""), null=True)
    Mean = models.FloatField(_(""), null=True)

    def __str__(self):
        return self.source


class sample(models.Model):
    handle = models.CharField(max_length=100, null=True, blank=True)
    destination= models.CharField(max_length=100, null=True, blank=True)
  
    def __str__(self):
        return self.handle
