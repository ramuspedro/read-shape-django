from django.urls import path

from .views import ShapeUploadRest

urlpatterns = [
  path('v1/shape-upload/', ShapeUploadRest.as_view()),
]