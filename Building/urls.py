from django.contrib import admin
from django.urls import path
from rest_framework import routers
from app.views import BuildingViewSet

router = routers.SimpleRouter()
router.register('buildings', BuildingViewSet, basename="buildings")

urlpatterns = [
    path('admin/', admin.site.urls),

]
urlpatterns += router.urls
