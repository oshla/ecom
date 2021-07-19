from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_Item)
admin.site.register(Shipping_Address)
""" admin.site.register(MoreUserInfo) """

