from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api import viewsets as carsViewSets

route = routers.DefaultRouter()
route.register(r'cars', carsViewSets.CarsViewSets, basename='Cars')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
