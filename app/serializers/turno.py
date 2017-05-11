from rest_framework import serializers
from app.models import Turno, Estadia

class CleanEstadiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadia
        exclude = ('turno',)
        depth = 1

class TurnoSerializer(serializers.ModelSerializer):
    estadias = CleanEstadiaSerializer(many=True)

    class Meta:
        model = Turno
        fields = '__all__'
        depth = 1

class PureTurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'
        