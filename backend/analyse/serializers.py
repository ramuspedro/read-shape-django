from rest_framework import serializers

from .models import ShapeUpload

class ShapeUploadSerializer(serializers.ModelSerializer):
  class Meta:
    model = ShapeUpload
    fields = '__all__'