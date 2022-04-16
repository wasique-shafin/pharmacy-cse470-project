from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


class ListingManager(models.Manager):
    def get_queryset(self):
        return super(ListingManager, self).get_queryset().filter(for_sale=True) # is_active => for_sale


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    details = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'      # categories => Categories

    def get_absolute_url(self):
        return reverse('MVC:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Listing(models.Model):
    category = models.ForeignKey(Category, related_name='listing', on_delete=models.CASCADE)
    #!OLD type0 = models.ForeignKey(Type,related_name='listing', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='listing_creator', on_delete=models.CASCADE)
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
        return reverse('MVC:listing_detail', args=[self.slug])   #was'store:product_detail' => MVC:listing_detail
    
    def __str__(self):
        return self.name


# class Order(models.Model):
#     type0 = models.ForeignKey(Type,related_name='orders', on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True)
#     date = models.DateTimeField(auto_now_add=True)
#     transaction = models.DecimalField(max_digits=8, decimal_places=2)
#     prescription = models.ImageField(upload_to='images/prescriptions')
#     is_valid = models.BooleanField(default=False)
#     is_complete = models.BooleanField(default=False)

#     class Meta:
#         verbose_name_plural = 'orders'

#     def __str__(self):
#         return self.name


# class Customer(models.Model):
#     name = models.CharField(max_length=255, db_index=True)
#     age = models.IntegerField()
#     email = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True)
#     image = models.ImageField(upload_to='images/customers')
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=25)
#     is_verified = models.BooleanField(default=False)

#     class Meta:
#         verbose_name_plural = 'customers'

#     def __str__(self):
#         return self.name


# class Employee(models.Model):
#     name = models.CharField(max_length=255, db_index=True)
#     email = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True)
#     image = models.ImageField(upload_to='images/employees')
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=25)
#     salary = models.DecimalField(max_digits=12, decimal_places=2)
#     log = models.TextField(blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'employees'

#     def __str__(self):
#         return self.name

# class Manager(models.Model):
#     name = models.CharField(max_length=255, db_index=True)
#     email = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True)
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=25)
    
#     class Meta:
#         verbose_name_plural = 'managers'

#     def __str__(self):
#         return self.name