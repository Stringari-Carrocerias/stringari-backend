from rest_framework.viewsets import ModelViewSet

from core.models import ModeloCarroceria
from core.serializers import ModeloCarroceriaSerializer

class ModeloCarroceriaViewSet(ModelViewSet):
    queryset = ModeloCarroceria.objects.all()
    serializer_class = ModeloCarroceriaSerializer