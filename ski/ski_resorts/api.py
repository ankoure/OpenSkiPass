from rest_framework import routers

from ski_resorts.views import (
    SkiAreaViewSet,
)

router = routers.DefaultRouter()
router.register(r"skiareas", SkiAreaViewSet)

urlpatterns = router.urls
