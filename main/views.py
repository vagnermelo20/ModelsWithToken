from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Endereco, Visitante
from .serializers import UsuarioSerializers, EnderecoSerializers, VisitanteSerializers

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers
    
class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializers
    
class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializers

