from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from core.views import (
    CategoriaViewSet,
    CostumerCNPJViewSet,
    CostumerCPFViewSet,
    ModeloCarroceriaViewSet,
    UserRegistrationView,
    UserViewSet,
)
from uploader.router import router as uploader_router

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'modelosCarrocerias', ModeloCarroceriaViewSet, basename='modelosCarrocerias')
router.register(r'categorias', CategoriaViewSet, basename='categorias')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/media/', include(uploader_router.urls)),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/doc/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # Autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Registro de usuários
    path('api/registro/', UserRegistrationView.as_view(), name='user_registration'),
    path('api/registro/cnpj/', CostumerCNPJViewSet.as_view(), name='costumer_cnpj_registration'),
    path('api/registro/cpf/', CostumerCPFViewSet.as_view(), name='costumer_cpf_registration'),
    # API
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
