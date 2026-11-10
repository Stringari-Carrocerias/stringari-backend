from .user import (
    UserSerializer,
    UserRegistrationSerializer,
    CostumerCNPJSerializer,
    CostumerCPFSerializer
)
from .carroceria.modeloCarroceria import (
    ModeloCarroceriaListSerializer,
    ModeloCarroceriaRetrieveSerializer,
    ModeloCarroceriaCreateUpdateSerializer
)
from .carroceria.categoria import CategoriaSerializer