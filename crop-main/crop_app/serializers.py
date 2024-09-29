from rest_framework import serializers
from .models import ImageModel  # Adjust to your actual model

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'
