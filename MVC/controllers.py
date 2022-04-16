from django.shortcuts import render

from django.shortcuts import get_object_or_404


from .models import Category, Listing, Cart # Product => Listing

# Context Processors
def categories(request):
    return {
        'categories': Category.objects.all()
    }


def listing_all(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', {'listings': listings})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    listings = Listing.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'listings': listings})


def listing_detail(request, listing_slug):
    listing = get_object_or_404(Listing, slug=listing_slug, for_sale=True)
    return render(request, 'listing.html', {'listing': listing})


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