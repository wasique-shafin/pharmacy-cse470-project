# from django.shortcuts import render

# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404

# from MVC.models import Listing

# from .cart import Cart

# def cart_summary(request):
#     cart = Cart(request)
#     return render(request, 'summary.html', {'cart': cart})

# def cart_add(request):
#     cart = Cart(request)
#     if request.POST.get('action') == 'post':
#         listing_id = int(request.POST.get('listingid'))
#         listing_qty = int(request.POST.get('listingqty'))
#         listing = get_object_or_404(Listing, id=listing_id)
#         cart.add(listing=listing, qty=listing_qty)

#         cartqty = cart.__len__()
#         response = JsonResponse({'qty': cartqty})
#         return response

# def cart_delete(request):
#     cart = Cart(request)
#     if request.POST.get('action') == 'post':
#         listing_id = int(request.POST.get('listingid'))
#         cart.delete(listing=listing_id)

#         cartqty = cart.__len__()
#         carttotal = cart.get_total_price()
#         response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
#         return response

# def cart_update(request):
#     cart = Cart(request)
#     if request.POST.get('action') == 'post':
#         listing_id = int(request.POST.get('listingid'))
#         listing_qty = int(request.POST.get('listingqty'))
#         cart.update(listing=listing_id, qty=listing_qty)

#         cartqty = cart.__len__()
#         carttotal = cart.get_total_price()
#         response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
#         return response

# # Context Processors
# def cart(request):
#     return {'cart': Cart(request)}