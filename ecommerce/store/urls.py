from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),

    path('checkout/', views.checkout, name='checkout'),
    path('att_item/', views.attItem, name='attItem'),
    path('processo_do_pedido/', views.processoDoPedido, name='processo_do_pedido'),
]