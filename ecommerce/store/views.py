from django.shortcuts import render
from .models import *

# Create your views here.

def store(request):
    produtos = Produto.objects.all()
    context = {'produtos':produtos}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        itens = pedido.itempedido_set.all()
    else:
        itens = []
    context = {'itens': itens}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context) 