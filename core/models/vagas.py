from django.db import models

class Vaga(models.Model):
    nome = models.CharField(max_length=45)
    salario = models.DecimalField(max_digits=7, decimal_places=2)
    descricao = models.CharField(max_length=1000)


    def __str__(self):
        f'{self.nome}'