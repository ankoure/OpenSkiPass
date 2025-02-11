from rest_framework_gis import serializers

from ski_resorts.models import skiarea


class SkiAreaSerializer(
    serializers.GeoFeatureModelSerializer,
):
    class Meta:
        fields = ("id", "name","passaffiliation","partnered","website")
        geo_field = "location"
        model = skiarea