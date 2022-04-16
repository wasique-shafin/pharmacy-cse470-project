from decimal import Decimal

from MVC.models import Listing


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, listing, qty):
        listing_id = str(listing.id)

        if listing_id in self.cart:
            self.cart[listing_id]['qty'] = qty
        else:
            self.cart[listing_id] = {'price': str(listing.price), 'qty': qty}

        self.save()

    def __iter__(self):
        listing_ids = self.cart.keys()
        listings = Listing.listings.filter(id__in=listing_ids)
        cart = self.cart.copy()

        for listing in listings:
            cart[str(listing.id)]['listing'] = listing

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    def update(self, listing, qty):
        listing_id = str(listing)
        if listing_id in self.cart:
            self.cart[listing_id]['qty'] = qty
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def delete(self, listing):
        listing_id = str(listing)

        if listing_id in self.cart:
            del self.cart[listing_id]
            print(listing_id)
            self.save()

    def save(self):
        self.session.modified = True
