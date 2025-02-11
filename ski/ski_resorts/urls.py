from django.urls import path
from . import views
from django.views.generic import TemplateView
from ski_resorts.views import MapView


urlpatterns = [
    path("", TemplateView.as_view(
            template_name="map.html"
            ),
        ),

]