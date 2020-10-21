from django.urls import path
from . import views # ambil semua store, cart dan checkout

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]

