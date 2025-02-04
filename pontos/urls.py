from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PontoColetaViewSet
from .views import mapa, adicionar_ponto, site

router = DefaultRouter()
router.register(r'pontos', PontoColetaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mapa/', mapa, name='mapa'),
    path('adicionar/', adicionar_ponto, name='adicionar_ponto'),
    path('coleta/', site, name='site'),
]