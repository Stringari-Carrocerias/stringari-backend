from rest_framework.viewsets import ModelViewSet

from core.models import Vaga
from core.serializers import VagaSerializer

class VagaViewSet(ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer