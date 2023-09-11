from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

from .models import *
from .utils import cookieCart, cartDados, pedidoVisitante

# Create your views here.

def store(request):

    dados = cartDados(request)
    itensCarrinho = dados['itensCarrinho']

    produtos = Produto.objects.all()
    banners = Banners.objects.all()
    informacao = Informacao.objects.all()
    context = {'produtos':produtos, 'itensCarrinho':itensCarrinho, 'banners':banners, 'informacao':informacao}
    return render(request, 'store/store.html', context)

def search(request):
    
    dados = cartDados(request)
    itensCarrinho = dados['itensCarrinho']

    banners = Banners.objects.all()
    informacao = Informacao.objects.all()
    search = request.GET.get('search','')
    produtos = Produto.objects.filter(nome__icontains= search)

    context = {'itensCarrinho':itensCarrinho, 'banners':banners, 'informacao':informacao, 'search':search, 'produtos':produtos}
    return render(request, 'store/search.html', context)

def cart(request):

    dados = cartDados(request)
    itensCarrinho = dados['itensCarrinho']
    itens = dados['itens']
    pedido = dados['pedido']

    context = {'itens': itens, 'pedido': pedido, 'itensCarrinho':itensCarrinho}
    return render(request, 'store/cart.html', context)


def checkout(request):
        
    dados = cartDados(request)
    itensCarrinho = dados['itensCarrinho']
    itens = dados['itens']
    pedido = dados['pedido']

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
    transacao_id = datetime.datetime.now().timestamp()
    dados = json.loads(request.body)

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)

    else:
        cliente, pedido = pedidoVisitante(request, dados)
            
    total = float(dados['form']['total'].replace(',', '.'))
    pedido.transacao_id = transacao_id

    if total == float(pedido.valor_total_carrinho):
        pedido.completo = True
        pedido.save()
    
    if pedido.envio == True:
        EnderecoEntrega.objects.create(
            cliente = cliente,
            pedido = pedido,
            endereco = dados['envio']['address'],
            cidade = dados['envio']['city'],
            estado = dados['envio']['state'],
            codigo_postal = dados['envio']['zipcode'], 
        )
    
    return JsonResponse("O pagamento foi realizado", safe=False)