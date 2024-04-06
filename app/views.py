from rest_framework import mixins, viewsets, filters
from app.serializers import BuildingSerializer
from app.models import Building


class BuildingViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
    ordering_fields = ['id']
    pagination_class = None
