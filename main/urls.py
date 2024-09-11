from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, EnderecoViewSet, VisitanteViewSet

router = DefaultRouter()
router.register(r'Usuario', UsuarioViewSet)
router.register(r'Endereco', EnderecoViewSet)
router.register(r'Visitante', VisitanteViewSet)

urlpatterns = [
    path('', include(router.urls))
]
