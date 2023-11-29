from rest_framework import serializers
from .models import SeuModelo

class SeuModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeuModelo
        fields = '__all__'
