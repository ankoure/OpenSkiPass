from django.urls import path
from . import views
from django.views.generic import TemplateView
from ski_resorts.views import MapView


urlpatterns = [
    path('ski_resorts/', views.landingpage, name='landingpage'),
    path("map/", MapView.as_view()),

]