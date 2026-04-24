from rest_framework.serializers import ModelSerializer
from core.models.carroceria.categoria import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nome']