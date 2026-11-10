from .user import (
    UserSerializer,
    UserRegistrationSerializer,
    CustomerCNPJSerializer,
    CustomerCPFSerializer
)
from .carroceria.modeloCarroceria import (
    ModeloCarroceriaListSerializer,
    ModeloCarroceriaRetrieveSerializer,
    ModeloCarroceriaCreateUpdateSerializer
)
from .carroceria.categoria import CategoriaSerializer