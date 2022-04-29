# Routes
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import controllers
from .controllers import (UserLoginForm)

app_name = 'MVC'

urlpatterns = [
     path('', controllers.listing_all, name='listing_all'),
     path('listing/<slug:listing_slug>/', controllers.listing_detail, name='listing_detail'),
     path('category/<slug:category_slug>/', controllers.category_list, name='category_list'),
     path('cart', controllers.cart_summary, name='cart_summary'),
     path('cart/add/', controllers.cart_add, name='cart_add'),
     path('cart/delete/', controllers.cart_delete, name='cart_delete'),
     path('cart/update/', controllers.cart_update, name='cart_update'),
     path('account/login/', auth_views.LoginView.as_view(template_name='account/registration/login.html',form_class=UserLoginForm), name='login'),
     path('account/logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
     path('account/register/', controllers.account_register, name='register'),
     path('account/dashboard/', controllers.dashboard, name='dashboard'),
     path('account/profile/edit/', controllers.edit_details, name='edit_details'),
     path('account/profile/delete_user/', controllers.delete_user, name='delete_user'),
     path('account/profile/delete_confirm/', TemplateView.as_view(template_name="account/user/delete_confirm.html"), name='delete_confirmation'),
]
