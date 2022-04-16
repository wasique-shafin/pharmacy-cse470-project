from django.shortcuts import render

from django.shortcuts import get_object_or_404

from .models import Category, Listing # Product => Listing


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def listing_all(request): # all_products => all_listings   #R all_listings => listing_all
    listings = Listing.objects.all()   # products => listings; Product => Listing
    return render(request, 'home.html', {'listings': listings}) # store/home.html => home.html; products => listings


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    listings = Listing.objects.filter(category=category) # products => listings;  Product => Listing
    return render(request, 'category.html', {'category': category, 'listings': listings}) # store/products/category.html => category.html


def listing_detail(request, listing_slug): # product_detail => listing_detail;  slug => listing_slug
    listing = get_object_or_404(Listing, slug=listing_slug, for_sale=True) # product => listing; Product => Listing; slug => listing_slug; is_active => for_sale
    return render(request, 'listing.html', {'listing': listing})  # store/products/detail.html => listing.html; product => listing