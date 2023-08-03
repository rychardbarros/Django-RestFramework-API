from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.api.serializers import CarsSerializer
from core import models

class CarsViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = CarsSerializer
    queryset = models.Cars.objects.all()
