from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Resort,skiarea

# Register your models here.
# class ResortAdmin(admin.ModelAdmin):
#   list_display = ("resortname",)
# admin.site.register(Resort,ResortAdmin)


class ResortAdmin(GISModelAdmin):
    list_display = ("resortname",)
admin.site.register(Resort,ResortAdmin)


class SkiAreaAdmin(GISModelAdmin):
    list_display = ("name","geom")
admin.site.register(skiarea,SkiAreaAdmin)