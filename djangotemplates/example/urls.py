from django.urls import path
from example import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'), # Notice the URL has been named
    path('about.html/', views.AboutPageView.as_view(), name='about'),
    path('cart.html/', views.CartPageView.as_view(), name='cart'),
    path('checkout.html/', views.CheckoutPageView.as_view(), name='checkout'),
    path('contact.html/', views.ContactPageView.as_view(), name='contact'),
    path('shop-single.html/', views.ShopsinglePageView.as_view(), name='shop-single'),
    path('shop.html/', views.ShopPageView.as_view(), name='shop'),
    path('thankyou.html/', views.ThankyouPageView.as_view(), name='thankyou'),
    
]