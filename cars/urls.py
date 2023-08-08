from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api import viewsets as carsViewSets
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView)


route = routers.DefaultRouter()
route.register(r'cars', carsViewSets.CarsViewSets, basename='Cars')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    # Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
