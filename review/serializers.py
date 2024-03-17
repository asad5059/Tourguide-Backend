from .models import PlaceInfoModel
from rest_framework import serializers

class PlaceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceInfoModel
        fields = ['id', 'name', 'address', 'rating', 'type', 'image']
        read_only_fields = ['owner']
        