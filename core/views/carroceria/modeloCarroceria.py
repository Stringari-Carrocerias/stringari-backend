# Import para Adicionar Filtros 
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from core.models import ModeloCarroceria
from core.serializers import ModeloCarroceriaListSerializer, ModeloCarroceriaRetrieveSerializer, ModeloCarroceriaCreateUpdateSerializer

class ModeloCarroceriaViewSet(ModelViewSet):
    queryset = ModeloCarroceria.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ModeloCarroceriaCreateUpdateSerializer
        if self.action == 'retrieve':
            return ModeloCarroceriaRetrieveSerializer
        return ModeloCarroceriaListSerializer

    # Código para filtros

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria']