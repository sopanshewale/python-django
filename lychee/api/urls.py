from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet, TemperatureViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'temperatures', TemperatureViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
