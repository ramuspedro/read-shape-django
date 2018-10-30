from django.shortcuts import render

# Create your views here.
from django.core import serializers
from rest_framework import generics

from .models import ShapeUpload
from .serializers import ShapeUploadSerializer

class ShapeUploadRest(generics.ListCreateAPIView):
  """ Test Upload Shape """
  queryset = ShapeUpload.objects.all()
  serializer_class = ShapeUploadSerializer

class AnalyseDenseForest(generics.CreateAPIView):
  """ Analyse Dense Forest """