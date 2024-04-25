# djangotemplates/example/views.py

from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class CartPageView(TemplateView):
    template_name = "cart.html"

class CheckoutPageView(TemplateView):
    template_name = "checkout.html"
class ContactPageView(TemplateView):
    template_name = "contact.html"

class ShopsinglePageView(TemplateView):
    template_name = "shop-single.html"    
class ShopPageView(TemplateView):
    template_name = "shop.html"
class ThankyouPageView(TemplateView):
    template_name = "thankyou.html"