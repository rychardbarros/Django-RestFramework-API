from rest_framework import viewsets
from core.api.serializers import CarsSerializer
from core import models

class CarsViewSets(viewsets.ModelViewSet):
    serializer_class = CarsSerializer
    queryset = models.Cars.objects.all()

