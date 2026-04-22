from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return f"({self.id}) {self.nome}"