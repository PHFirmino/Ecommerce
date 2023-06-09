from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200, null=True)
    preco = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    #imagem

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    completo = models.BooleanField(default=False, null=True, blank=False)
    transacao_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
    quantidade = models.IntegerField(default=0, null=True, blank=False)
    data_add = models.DateTimeField(auto_now_add=True)

    #def__str__(self):
        #return self.produto.nome

class EnderecoEntrega(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
    endereco = models.CharField(max_length=200, null=True)
    cidade = models.CharField(max_length=200, null=True)
    estado = models.CharField(max_length=200, null=True)
    codigo_postal = models.CharField(max_length=200, null=True)
    data_add = models.DateTimeField(auto_now_add=True)