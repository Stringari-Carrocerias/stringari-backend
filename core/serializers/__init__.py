from .user import UserRegistrationSerializer, UserSerializer
from .carroceria.modeloCarroceria import (
    ModeloCarroceriaListSerializer,
    ModeloCarroceriaRetrieveSerializer,
    ModeloCarroceriaCreateUpdateSerializer
)
from .carroceria.categoria import CategoriaSerializer
from .vagas import VagaSerializer