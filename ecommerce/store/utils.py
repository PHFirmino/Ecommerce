import json
from .models import *

def cookieCart(request):
    try:
        carrinho = json.loads(request.COOKIES['carrinho'])
    except:
        carrinho = {}
    print('Carrinho: ', carrinho)
    itens = []
    pedido = {'valor_total_itens': 0, 'valor_total_carrinho':0, 'envio': False}
    itensCarrinho = pedido['valor_total_itens']

    for i in carrinho:
        try:
            itensCarrinho += carrinho[i]["quantidade"]

            produto = Produto.objects.get(id=i)
            total = (produto.preco * carrinho[i]["quantidade"])

            pedido['valor_total_carrinho'] += total
            pedido['valor_total_itens'] += carrinho[i]["quantidade"]

            item = {
                'produto':{
                    'id': produto.id,
                    'nome': produto.nome,
                    'preco': produto.preco,
                    'imagemURL': produto.imagemURL,
                },
            'quantidade': carrinho[i]["quantidade"],
            'valor_total': total
            }
            itens.append(item)

            if produto.digital == False:
                pedido['envio'] = True
        except:
            pass
    return {'itens': itens, 'pedido': pedido, 'itensCarrinho':itensCarrinho}

def cartDados(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        itens = pedido.itempedido_set.all()
        itensCarrinho = pedido.valor_total_itens
    else:
        cookieDados = cookieCart(request)
        itensCarrinho = cookieDados['itensCarrinho']
        itens = cookieDados['itens']
        pedido = cookieDados['pedido']
    return {'itens': itens, 'pedido': pedido, 'itensCarrinho':itensCarrinho}

def pedidoVisitante(request, dados):
        print('Usuário não está logado')

        print('COOKIES: ', request.COOKIES)
        nome = dados['form']['name']
        email = dados['form']['email']

        cookieDados = cookieCart(request)
        itens = cookieDados['itens']

        cliente, created = Cliente.objects.get_or_create(
            email = email,
        )
        cliente.nome = nome
        cliente.save()

        pedido = Pedido.objects.create(
            cliente = cliente,
            completo = False,
        )

        for item in itens:
            produto = Produto.objects.get(id=item['produto']['id'])

            itemPedido = ItemPedido.objects.create(
                produto = produto,
                pedido = pedido,
                quantidade = item['quantidade'],
            )
        return cliente, pedido
