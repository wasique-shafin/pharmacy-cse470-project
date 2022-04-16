from django.shortcuts import render

from django.shortcuts import get_object_or_404


from .models import Category, Listing, Cart # Product => Listing


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

from django.http import JsonResponse

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'summary.html', {'cart': cart})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        listing_id = int(request.POST.get('listingid'))
        listing_qty = int(request.POST.get('listingqty'))
        listing = get_object_or_404(Listing, id=listing_id)
        cart.add(listing=listing, qty=listing_qty)

        cartqty = cart.__len__()
        response = JsonResponse({'qty': cartqty})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        listing_id = int(request.POST.get('listingid'))
        cart.delete(listing=listing_id)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        listing_id = int(request.POST.get('listingid'))
        listing_qty = int(request.POST.get('listingqty'))
        cart.update(listing=listing_id, qty=listing_qty)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
        return response

# Context Processors
def cart(request):
    return {'cart': Cart(request)}