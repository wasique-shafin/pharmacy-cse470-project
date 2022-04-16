# Routes
from django.urls import path

from . import controllers

app_name = 'MVC'

urlpatterns = [
     path('', controllers.listing_all, name='listing_all'),
     path('listing/<slug:listing_slug>/', controllers.listing_detail, name='listing_detail'),
     path('category/<slug:category_slug>/', controllers.category_list, name='category_list'),
     path('cart', controllers.cart_summary, name='cart_summary'),
     path('cart/add/', controllers.cart_add, name='cart_add'),
     path('cart/delete/', controllers.cart_delete, name='cart_delete'),
     path('cart/update/', controllers.cart_update, name='cart_update'),
]