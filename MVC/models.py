from django.db import models

from django.urls import reverse
from django.conf import settings

class ListingManager(models.Manager):
    def get_queryset(self):
        return super(ListingManager, self).get_queryset().filter(for_sale=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    details = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('MVC:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Listing(models.Model):
    category = models.ForeignKey(Category, related_name='listing', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='listing_creator', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/listings', default='images/default.png')
    inventory = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    for_sale = models.BooleanField(default=True)
    details = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    need_prescription = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    listings = ListingManager()

    class Meta:
        verbose_name_plural = 'Listings'
    
    def get_absolute_url(self):
        return reverse('MVC:listing_detail', args=[self.slug])
    
    def __str__(self):
        return self.name


from decimal import Decimal

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

    def get_subtotal_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def get_total_price(self):
        return (sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())+50)

    def delete(self, listing):
        listing_id = str(listing)

        if listing_id in self.cart:
            del self.cart[listing_id]
            print(listing_id)
            self.save()

    def save(self):
        self.session.modified = True
