from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api import viewsets as carsViewSets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


route = routers.DefaultRouter()
route.register(r'cars', carsViewSets.CarsViewSets, basename='Cars')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
