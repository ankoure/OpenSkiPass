from django.urls import path
from . import views

urlpatterns = [
    path('ski_resorts/', views.landingpage, name='landingpage'),
]