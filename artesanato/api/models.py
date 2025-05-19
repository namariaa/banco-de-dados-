from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    telefone = models.IntegerField()
    redeSocialLink = models.URLField()

class Endereco(models.Model):
    rua = models.CharField(max_length=250)
    nuemero = models.IntegerField()
    bairro = models.CharField(max_length=250)
    cidade = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    cep = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Servico(models.Model):
    nome = models.CharField(max_length=250)
    valor = models.FloatField()
    tempoPrevisto = models.DateTimeField()

class FormaPagamento(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=500)
    taxa = models.FloatField()

class Pedido(models.Model):
    SITUACAO = (("pg","pago"), ("op", "aberto"), ("cc", "cancelado"))
    situacao = models.CharField(max_length=250, choices=SITUACAO)
    descricao = models.CharField(max_length=500)
    valorAssociado = models.FloatField()
    valorTotal = models.FloatField()
    taxaExtra = models.FloatField()
    dataRecebimento = models.DateTimeField()
    dataEntrega = models.DateTimeField()
    formaPagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

class Relacao(models.Model):
    pessoa1 = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="Relacionamento")
    pessoa2 = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=250)
    parentesco = models.CharField(max_length=250)
