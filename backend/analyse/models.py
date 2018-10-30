from django.contrib.gis.db import models

# Create your models here.
class ShapeUpload(models.Model):
  name = models.CharField(max_length=200)
  the_geom = models.GeometryField()
  # the_geom = models.PointField()

  def __str__(self):
    return self.name