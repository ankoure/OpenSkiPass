from django.http import HttpResponse
from django.template import loader
from ski_resorts.models import skiarea
import json
from django.core.serializers import serialize
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework_gis import filters
from ski_resorts.serializers import (
    SkiAreaSerializer,
)

def landingpage(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

class MapView(ListView):
    context_object_name = "markers"
    model = skiarea
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs
        )
        context["markers"] = json.loads(
            serialize(
                "geojson", context["markers"]
            )
        )
        return context
    

class SkiAreaViewSet(
    viewsets.ReadOnlyModelViewSet,
):
    bbox_filter_field = "location"
    filter_backends = [filters.InBBoxFilter]
    queryset = skiarea.objects.filter(operatingstatus = 'operating', alpine=True)
    serializer_class = SkiAreaSerializer
