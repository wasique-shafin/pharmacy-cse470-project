# Routes
from django.urls import path

from . import controllers     # views => controllers

app_name = 'MVC' # must match with namespace=`MVC` in core/urls.py

urlpatterns = [
     path('', controllers.listing_all, name='listing_all'), # all_products => all_listings; views => Controller
     path('listing/<slug:listing_slug>/', controllers.listing_detail, name='listing_detail'), # item => listing # product_detail => listing_detail; views => Controller; slug => listing_slug
     path('category/<slug:category_slug>/', controllers.category_list, name='category_list'), # views => Controller; search => category
]