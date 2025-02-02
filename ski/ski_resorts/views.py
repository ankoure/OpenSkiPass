from django.http import HttpResponse
from django.template import loader
from ski_resorts.models import Resort
import json
from django.core.serializers import serialize
from django.views.generic import ListView

def landingpage(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

class MapView(ListView):
    context_object_name = "markers"
    model = Resort
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