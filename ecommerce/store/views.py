from django.shortcuts import render
from django.http import JsonResponse
import json


from .models import *

# Create your views here.

def store(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        itens = pedido.itempedido_set.all()
        itensCarrinho = pedido.valor_total_itens
    else:
        itens = []
<<<<<<< HEAD
        pedido = {'valor_total_itens': 0, 'valor_total_carrinho':0, 'envio': False}
=======
        pedido = {'valor_total_itens': 0, 'valor_total_carrinho':0}
>>>>>>> a86bbfc1860337376379261913b264ad06754bb7
        itensCarrinho = pedido['valor_total_itens']

    produtos = Produto.objects.all()
    context = {'produtos':produtos, 'itensCarrinho':itensCarrinho}
    return render(request, 'store/store.html', context)

def cart(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        itens = pedido.itempedido_set.all()
        itensCarrinho = pedido.valor_total_itens
    else:
        itens = []
<<<<<<< HEAD
        pedido = {'valor_total_itens': 0, 'valor_total_carrinho':0, 'envio': False}
        itensCarrinho = pedido['valor_total_itens']
=======
        itensCarrinho = pedido['valor_total_itens']
        pedido = {'valor_total_itens': 0, 'valor_total_carrinho':0}
>>>>>>> a86bbfc1860337376379261913b264ad06754bb7

    context = {'itens': itens, 'pedido': pedido, 'itensCarrinho':itensCarrinho}

    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        itens = pedido.itempedido_set.all()
        itensCarrinho = pedido.valor_total_itens
    else:
        itens = []
<<<<<<< HEAD
        pedido = {'valor_total_itens': 0, 'valor_total_carrinho':0, 'envio': False}
        itensCarrinho = pedido['valor_total_itens']
=======
        itensCarrinho = pedido['valor_total_itens']
        pedido = {'valor_total_itens': 0, 'valor_total_carrinho':0}
>>>>>>> a86bbfc1860337376379261913b264ad06754bb7

    context = {'itens': itens, 'pedido': pedido, 'itensCarrinho':itensCarrinho}

    return render(request, 'store/checkout.html', context) 

def attItem(request):
    dados = json.loads(request.body)
    produtoID = dados['produtoID']
    produtoAcao = dados['produtoAcao']

    print('Ação:', produtoAcao)
    print('Produto ID:', produtoID)

    cliente = request.user.cliente
    produto = Produto.objects.get(id=produtoID)
    pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
    itemPedido, created = ItemPedido.objects.get_or_create(pedido=pedido, produto=produto)

    if produtoAcao == 'add':
        itemPedido.quantidade = (itemPedido.quantidade + 1)
    elif produtoAcao == 'remover':
        itemPedido.quantidade = (itemPedido.quantidade - 1)

    itemPedido.save()

    if itemPedido.quantidade <= 0:
        itemPedido.delete()

    return JsonResponse("Item foi adicionado", safe=False)

def processoDoPedido(request):
    print('Dados: ', request.body)
    return JsonResponse("O pagamento foi realizado", safe=False)