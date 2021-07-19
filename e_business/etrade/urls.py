
from django.urls import path
from etrade import views

urlpatterns = [
    path('', views.store, name='store'),
    path('checkout', views.checkout, name='checkout'),
    path('cart', views.cart, name='cart'),
    path('update_item', views.UpdateItem, name='update_item'),
    path('process_order', views.processOrder, name='process_order'),
    path('register', views.Register, name='register'),
    path('login', views.Login, name='login'),
    path('clientlogin', views.get_client_ip, name='sinzu'),
    path('logout', views.Logout, name='logout'),
    path('Equipment', views.equipmentsort, name='Equipment'),
    path('Livestock', views.livestocksort, name='Livestock'),
    path('Feed', views.feedsort, name='Feed'),
    path('Seedling', views.seedlingsort, name='Seedling'),
]
