# Routes
from django.urls import path

from . import controllers     # views => controllers

app_name = 'MVC' # must match with namespace=`MVC` in core/urls.py

urlpatterns = [
     path('', controllers.listing_all, name='listing_all'), # all_products => all_listings; views => Controller
     path('listing/<slug:listing_slug>/', controllers.listing_detail, name='listing_detail'), # item => listing # product_detail => listing_detail; views => Controller; slug => listing_slug
     path('category/<slug:category_slug>/', controllers.category_list, name='category_list'), # views => Controller; search => category
     path('cart', controllers.cart_summary, name='cart_summary'),
     path('cart/add/', controllers.cart_add, name='cart_add'),
     path('cart/delete/', controllers.cart_delete, name='cart_delete'),
     path('cart/update/', controllers.cart_update, name='cart_update'),
]