from django.db import models
from uploader.models import Image
from .categoria import Categoria

class ModeloCarroceria(models.Model):
    nome = models.CharField(max_length=255, null = True, blank = True)
    valor = models.DecimalField(max_digits=12, decimal_places = 2, null=True, blank=True)
    comprimento = models.DecimalField(max_digits=4, decimal_places = 2, null=True, blank=True)
    largura = models.DecimalField(max_digits=4, decimal_places = 2, null=True, blank=True)
    altura = models.DecimalField(max_digits=4, decimal_places = 2, null=True, blank=True)
    descricao = models.CharField(max_length=255, null = True, blank = True)
    descricaoCurta = models.CharField(max_length=100, null = True, blank = True)
    imagem = models.ForeignKey(Image, related_name='+', on_delete=models.PROTECT, default=None)
    categoria = models.ForeignKey(Categoria, related_name='categoria', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'Modelo Carroceria'
        verbose_name_plural = 'Modelos Carrocerias'

    def __str__(self):
        return f'{self.nome}'