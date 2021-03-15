from rest_framework import serializers
from appCompradores.models import Compradores

class CompradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compradores
        fields = ('id','nombre','apellido','direccion','ciudad','longitud','latitud','estado_geo')