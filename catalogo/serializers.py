from rest_framework import serializers
from .models import conteudo, Categoria

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ConteudoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializers()

    class Meta:
        model = conteudo
        fields = '__all__'