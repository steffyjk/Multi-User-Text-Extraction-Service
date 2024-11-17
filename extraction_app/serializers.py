from rest_framework import serializers
from .models import DocumentDetails

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentDetails
        fields = '__all__'