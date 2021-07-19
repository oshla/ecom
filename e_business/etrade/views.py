from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import *
import datetime
from . utils import cookieCart, cartData, guestOrder
from .Recommendersys.process import getUsername
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import auth
from django.contrib import messages
from .models import Customer, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
# from .Recommendersys import process





def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            Customer=customer, complete=False)
        items = order.order_item_set.all()
        cartitems = order.get_cart_items
    else:
       cookieData = cookieCart(request)
       cartitems = cookieData['cartitems']

    products= Product.objects.all()
    context = {'products': products, 'cartitems': cartitems}
    return render(request, 'etrade/store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        #order_item_set.all() is my model Order_Item but in small letter. this gave me a tough time trying to figure out the bloody error
        items = order.order_item_set.all()
        cartitems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartitems = cookieData['cartitems']
        order = cookieData['order']
        items = cookieData['items']
                
            
    context = {'items':items, 'order':order, 'cartitems':cartitems}
    return render(request, 'etrade/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            Customer=customer, complete=False)
        items = order.order_item_set.all()
        cartitems = order.get_cart_items
        #
        # folashads = Order.objects.get(username='folashads')
        # itemzz = Order_Item.objects.filter(Order=folashads)
        logged_user = Customer.objects.get(user=request.user)
        person=logged_user.sc_handle
        print('bvjkbmb')
        friend = getUsername(person)
        print('wsxw')
        print(friend)
        friend_user = Customer.objects.get(sc_handle=friend)
        itemzz = Order_Item.objects.filter(Order__Customer__sc_handle=friend)
    else:
        cookieData = cookieCart(request)
        cartitems = cookieData['cartitems']
        order = cookieData['order']
        items = cookieData['items']

        """  folashads = Order.objects.get(username='folashads')
        itemzz = Order_Item.objects.filter(Order=folashads) """
    context = {'items': items, 'order': order, 'cartitems':cartitems, 'itemzz': itemzz,'friend_user':friend_user}
    print(items)
    
    return render(request, 'etrade/checkout.html', context)


def UpdateItem(request):
    data= json.loads(request.body)
    Productid = data['Productid']
    action= data['action']

    print('Action:', action)
    print('Productid:', Productid)
    print(data)

    customer = request.user.customer
    product= Product.objects.get(id=Productid)
    order, created = Order.objects.get_or_create(Customer=customer, complete=False)
    orderitem, created = Order_Item.objects.get_or_create(Order=order, Product=product)

    if action == 'add':
        orderitem.quantity= (orderitem.quantity + 1)
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)
    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse("The Item has been added", safe=False)

""" def processOrder(request):
    #print('data:', request.body)
    transaction_id= datetime.datetime.now().timestamp()
    data= json.loads(request.body)
    print(data)

    if request.user.is_authenticated:
        customer= request.user.customer
        order = Order.objects.get(Customer=customer, complete=False)
        total= float(data['form']['total'])
        print(order.get_cart_total)
        if total == order.get_cart_total:
            order.complete = True
            print("heeezzzzzzzzzzzzzzzzzzzzzzzz")
        order.save()
        if order.shipping == True:

            print("heeezzzzzzzzzzzzzzzzzzzzzzzz")
            Shipping_Address.objects.create(
                #some attributes here were already defined in the checkout.html file
                Customer=customer,
                Order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )     
    else:
        print('User is not signed in...')
    return JsonResponse("Payment completed successfully", safe=False)
 """

def processOrder(request):
    #print('data:', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        if order.shipping == True:
            Shipping_Address.objects.create(
                #some attributes here were already defined in the checkout.html file
                Customer=customer,
                Order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        customer, order = guestOrder(request, data)
        #i put this code in a function just to make things easier. uncomment if any future error occurs or when the product id finally appears
        """ print('User is not signed in...')
        print("COOKIES:", request.COOKIES)
        name = data['form']['name']
        email= data['form']['email']

        cookieData= cookieCart(request)
        items= cookieData['items']

        customer, created = Customer.objects.get_or_create(email=email,)
        customer.name=name
        customer.save()

        order= Order.objects.create(customer=customer, complete=False,)

        for item in items:
            product = Product.objects.get(id=item['product']['id'])

            orderitem = Order_Item.objects.create(product=product,order=order, quantity=item['quantity']) """

    """ total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save() 

     if order.shipping == True:
            Shipping_Address.objects.create(
                #some attributes here were already defined in the checkout.html file
                Customer=customer,
                Order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            ) """



    return JsonResponse("Payment completed successfully", safe=False)


def Register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        age = request.POST['age']
        password = request.POST['password']
        email = request.POST['email']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        marital_status = request.POST['marital_status']
        sc_handle = request.POST['sc_handle']
        edu_qualification = request.POST['edu_qualification']
        occupation = request.POST['occupation']
        state_of_origin = request.POST['state_of_origin']
        country = request.POST['country']
        User.objects.create_user(username=email,email=email,password=password)
        user = User.objects.get(username=email, email=email)
        cus=Customer(user=user,first_name=first_name,last_name=last_name,gender=gender,age=age,email=email,address=address,phone_number=phone_number,marital_status=marital_status,sc_handle=sc_handle,edu_qualification=edu_qualification,occupation=occupation,state_of_origin=state_of_origin,country=country)
        cus.save()
        emailfrom = settings.EMAIL_HOST_USER
        subject = "registration complete!"
        message = "thanks for choosing us!!!"
        emailto = email
        recipient = [emailto,]
        #send_mail(subject, message, emailfrom, recipient, fail_silently=True)
        
        mg = "Registration successful"
        return render(request, 'etrade/login.html', {"mg":mg})

    else:
        messages.info(request, 'invalid form')
        return render(request, 'etrade/registration.html')

def equipmentsort(request):
 

    pro = Product.objects.filter(category="equipment")
    return render(request, 'etrade/store.html',{"products": pro})

def livestocksort(request):
    pro = Product.objects.filter(category="livestock")
    return render(request, 'etrade/store.html',{"products":pro})

def feedsort(request):
  
    pro = Product.objects.filter(category="feed")
    return render(request, 'etrade/store.html',{"products": pro})


def seedlingsort(request):
    pro = Product.objects.filter(category="seedling")
    return render(request, 'etrade/store.html', {"products": pro})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('USERDOMAIN')
    User.objects.create_user(username=ip,password='password')
    user = User.objects.get(username=ip)
    cus = Customer(user=user)
    cus.save()
    user = auth.authenticate(
        username=ip, password='password')
    if user is not None and Customer.objects.get(user=user):
        auth.login(request, user)
        return redirect("store")
    else:
        messages.success(request, ("An error occurred, please try again!"))
        return render(request, 'etrade/login.html', {})

def Login(request):

   
    if request.method == "POST":
        email = request.POST['email']
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None and Customer.objects.get(user=user):
            auth.login(request, user)
            logged_user = Customer.objects.get(user=user)
            person = logged_user.sc_handle
            print(person)
            messages.success(request, ("welcome! {}".format(email)),  extra_tags='alert')
            return redirect("store")
        else:
            m = "An error occurred, please try again!"
            return render(request, 'etrade/login.html', {"m": m})
    else:
        return render(request, 'etrade/login.html', {})

 



def Logout(request):
    auth.logout(request)
    messages.success(request, ("You have been successfully logged out.."))
    """ print(process.c) """
    return redirect("login")
    pass




