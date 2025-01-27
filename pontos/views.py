from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import PontoColeta
from .serializers import PontoColetaSerializer
from django.shortcuts import render
import folium
from .models import PontoColeta

# Create your views here.

class PontoColetaViewSet(ModelViewSet):
    queryset = PontoColeta.objects.all()
    serializer_class = PontoColetaSerializer


def mapa(request):
    mapa = folium.Map(location=[-15.7801, -47.9292], zoom_start=5)  # Localização inicial (Brasil)

    pontos = PontoColeta.objects.all()
    for ponto in pontos:
        folium.Marker(
            location=[ponto.latitude, ponto.longitude],
            popup=f"<b>{ponto.nome}</b><br>{ponto.descricao}<br>{ponto.endereco}",
            icon=folium.Icon(color="green", icon="info-sign"),
        ).add_to(mapa)

    mapa_html = mapa._repr_html_()
    return render(request, 'pontos/mapa.html', {'mapa': mapa_html})