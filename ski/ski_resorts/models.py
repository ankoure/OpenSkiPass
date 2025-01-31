from django.contrib.gis.db import models
from django.contrib.gis.db.models import PointField

# Create your models here.
class Resort(models.Model):
    id = models.AutoField(primary_key=True)
    resortname = models.CharField(max_length=255)
    skimapurl = models.CharField(max_length=255)
    location = models.PointField(null=True, blank=True)  # Stores a single point (latitude/longitude)

    
    def __str__(self):
        return f"{self.resortname}"