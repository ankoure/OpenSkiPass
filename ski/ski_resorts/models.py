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
    geom = models.PointField(null=True, blank=True)  # Stores a single point (latitude/longitude)

    def __str__(self):
        return f"{self.name}"

class ski_area_isochrone:
    isochrone_pk = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    ski_area = models.ForeignKey(skiarea, on_delete=models.CASCADE)
    contour = models.IntegerField()
    geom = models.PolygonField()
    


class aerialway(models.Model):
    aerialway_pk = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    # populated by values found here: https://wiki.openstreetmap.org/wiki/Key:aerialway?uselang=en
    # exclude zip_line, goods, pylon, station
    aerialway_type = models.CharField(null=True)
    #j-bar, platter, and rope_tow imply 1 while t-bar implies 2, all else variable
    occupancy = models.IntegerField(null=True)
    #people per hour, numeric
    capacity = models.IntegerField(null=True)
    #Average journey time in minutes
    duration = models.IntegerField(null=True)
    #gondola,chairlift,mixed_lift imply yes, but cable_car, t-bar, j-bar, platter, rope_tow and magic carper imply no
    detachable = models.BooleanField(null=True)
    #only common for chair_lift
    bubble = models.BooleanField(default=False)
    heating = models.BooleanField(default=False)
    geom = models.LineStringField()
    ski_area = models.ForeignKey(skiarea,on_delete=models.CASCADE)


class trail(models.Model):
    trail_pk = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    name = models.CharField(null=True)
    difficulty = models.CharField(null=True)
    grooming = models.CharField(null=True)
    lit = models.BooleanField(null=True)
    piste_type = models.CharField(null=True)
    geom = models.LineStringField()
    ski_area = models.ForeignKey(skiarea,on_delete=models.CASCADE)

#osm piste:type = downhill, gladed = yes, and area = yes
class glade(models.Model):
    glade_pk = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    name = models.CharField(null=True)
    difficulty = models.CharField(null=True)
    piste_type = models.CharField(null=True)
    geom = models.PolygonField()
    ski_area = models.ForeignKey(skiarea,on_delete=models.CASCADE)


###############################################################################################################################################################################################################
#TODO: Later add logic to track ski passes, and associate with trails/lifts



###############################################################################################################################################################################################################

#Conform to ISO 4217 https://en.wikipedia.org/wiki/ISO_4217
#TODO: Add Logic to link https://developer.visa.com/capabilities/foreign_exchange/reference#tag/Foreign-Exchange-Rates-API/operation/ForeignExchangeRates_v2%20-%20Latest
# class currency(models.Model):
#     currency_pk = models.UUIDField( 
#          primary_key = True, 
#          default = uuid.uuid4, 
#          editable = False) 
#     code_str = models.CharField(max_length=3)
#     code_num = models.IntegerField()
#     currency_name = models.CharField()
#     active = models.BooleanField()


# class downhill_ski_pass(models.Model):
#     downhillpass_pk = models.UUIDField( 
#          primary_key = True, 
#          default = uuid.uuid4, 
#          editable = False)
#     # I.e Half Day Pass/Weekend Full Day/Holiday Halfday/Week night
#     name = models.CharField() 
#     price = models.FloatField()
#     currency = models.ForeignKey(currency, on_delete=models.CASCADE)
#     #I.e 24-25, 25-26
#     season = models.CharField()
#     #start and end time example: 9am - 4pm, 9am-12pm,etc. 
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     #does pass allow acess to whole mountain? or only certain areas? TODO: In future add if false then associate with lifts/trails provided
#     full_access = models.BooleanField()
#     ski_area = models.ForeignKey(skiarea, on_delete=models.CASCADE)


# class uphill_ski_pass(models.Model):
#     uphillpass_pk = models.UUIDField( 
#          primary_key = True, 
#          default = uuid.uuid4, 
#          editable = False)
#     price = models.FloatField()
#     currency = models.ForeignKey(currency, on_delete=models.CASCADE)
#     #I.e 24-25, 25-26
#     season = models.CharField()
#     ski_area = models.ForeignKey(skiarea, on_delete=models.CASCADE)

# class uphill_ski_route(models.Model):
#     uphillroute_pk = models.UUIDField( 
#          primary_key = True, 
#          default = uuid.uuid4, 
#          editable = False)
#     uphill_ski_pass = models.ForeignKey(uphill_ski_pass, on_delete=models.CASCADE)
#     geom = models.LineStringField()

