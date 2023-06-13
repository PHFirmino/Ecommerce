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
        pedido = {'valor_total_itens': 0, 'valor_total_carrinho':0}

    context = {'itens': itens, 'pedido': pedido}

    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        itens = pedido.itempedido_set.all()
    else:
        itens = []
        pedido = {'valor_total_itens': 0, 'valor_total_carrinho':0}

    context = {'itens': itens, 'pedido': pedido}

    return render(request, 'store/checkout.html', context) 