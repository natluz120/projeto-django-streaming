from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Categoria, conteudo 
from .serializers import CategoriaSerializers, ConteudoSerializer

class ConteudoViewSet(viewsets.ModelViewSet):
    queryset = conteudo.objects.all()
    serialize_class = ConteudoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serialize_class = CategoriaSerializers