from .models import *
from rest_framework.serializers import ModelSerializer

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
        