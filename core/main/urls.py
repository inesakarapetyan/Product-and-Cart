from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add'),
    path('delete_from_cart/', views.delete_from_cart,name='delete'),
    path('login/', views.login_request, name='login'),
    path('register/',views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('pay/', views.pay, name='pay'),
    path('deliver/', views.delivery, name='deliver'),
    path('address_after_payment/', views.user_details, name='address'),

]