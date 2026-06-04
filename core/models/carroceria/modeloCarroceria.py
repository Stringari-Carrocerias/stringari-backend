from django.db import models
from uploader.models import Image
from .categoria import Categoria

class ModeloCarroceria(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=12, decimal_places = 2)
    comprimento = models.DecimalField(max_digits=4, decimal_places = 2)
    largura = models.DecimalField(max_digits=4, decimal_places = 2)
    altura = models.DecimalField(max_digits=4, decimal_places = 2)
    descricao = models.CharField(max_length=255)
    descricaoCurta = models.CharField(max_length=100)
    imagem = models.ForeignKey(Image, related_name='+', on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, related_name='categoria', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'ModeloCarroceria'
        verbose_name_plural = 'ModelosCarrocerias'

    def __str__(self):
        return f'{self.nome}'