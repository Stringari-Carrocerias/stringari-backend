# Import para Adicionar Filtros 
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from core.models import ModeloCarroceria
from core.serializers import ModeloCarroceriaSerializer

class ModeloCarroceriaViewSet(ModelViewSet):
    queryset = ModeloCarroceria.objects.all()
    serializer_class = ModeloCarroceriaSerializer

    # Código para filtros

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria']