from random import choices
from statistics import quantiles
from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel
from produto.models import Produto
from django.urls import reverse_lazy

# Create your models here.

MOVIMENTO =(
    ('e', 'entrada'),
    ('s', 'saida'),
)

class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))

    def get_absolute_url(self):
        return reverse_lazy("estoque:estoque_entrada_detail", kwargs={"pk": self.pk})
    
    def nf_formatetd(self):
        return str(self.nf).zfill(4)

class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto=models.ForeignKey(Produto, on_delete=models.CASCADE)   
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveBigIntegerField()
    
    class Meta:
        ordering = ('pk',)

    def __str__(self) -> str:
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)