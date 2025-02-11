from django.contrib.gis.db import models
from django.contrib.gis.db.models import PointField
import uuid

# Create your models here.
class Resort(models.Model):
    id = models.AutoField(primary_key=True)
    resortname = models.CharField(max_length=255)
    skimapurl = models.CharField(max_length=255)
    location = models.PointField(null=True, blank=True)  # Stores a single point (latitude/longitude)

    
    def __str__(self):
        return f"{self.resortname}"
    

class skiarea(models.Model):
    skiarea_pk = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    id = models.IntegerField(null=True)
    scalerank = models.IntegerField(null=True)
    passaffiliation = models.CharField(max_length=255, null=True, default='Unaffiliated')
    partnered = models.BooleanField(null=True)
    name = models.CharField(max_length=255, null=True)
    operatingstatus = models.CharField(max_length=255, null=True)
    alpine = models.BooleanField(null=True)
    nordic = models.BooleanField(null=True)
    website = models.CharField(null=True)
    location = models.PointField(null=True, blank=True)  # Stores a single point (latitude/longitude)

    def __str__(self):
        return f"{self.name}"
    