"""
URL configuration for djangotemplates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


from example.views import (
    HomePageView,
    AboutPageView,
    CartPageView,
    CheckoutPageView,
    ContactPageView,
    ShopsinglePageView,
    ShopPageView,
    ThankyouPageView,
)

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', include('example.urls')) ,
    path('', HomePageView.as_view(), name='index'),
    path('about.html/', AboutPageView.as_view(), name='about'),
    path('cart.html/', CartPageView.as_view(), name='cart'),
    path('checkout.html/', CheckoutPageView.as_view(), name='checkout'),
    path('contact.html/', ContactPageView.as_view(), name='contact'),
    path('shop-single.html/', ShopsinglePageView.as_view(), name='shop-single'),
    path('shop.html/', ShopPageView.as_view(), name='shop'),
    path('thankyou.html/', ThankyouPageView.as_view(), name='thankyou'),
    # Add other URL patterns as needed
]

