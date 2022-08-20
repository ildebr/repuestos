from rest_framework import serializers
from .models import Repuestos, Venta, Reporte

class RepuestosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuestos
        fields = ('categoria', 'nombre', 'descripcion', 'precio_venta', 'unidades_disponible',)

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ('repuesto', 'cantidad', 'fecha_venta', 'total',)

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = ('fecha_inicio', 'fecha_fin','ventas',)