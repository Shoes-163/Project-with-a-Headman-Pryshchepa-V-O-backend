from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView # type: ignore
from . import views

router = routers.DefaultRouter()
router.register(
    'devices', views.DevicesViewSet, basename='devices'
    )
router.register(
    'metrics', views.MetricsViewSet, basename='metrics'
    )
urlpatterns = [
    path("api/", include(router.urls), name="api"),
    path('api/schema/', SpectacularAPIView.as_view(),
         name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),
]