from rest_framework.serializers import ModelSerializer
from .models import Disease

class DiseaseSerializer(ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'
