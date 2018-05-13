from django.contrib import admin
from django.urls import path, include
from lychee.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('temperature/', include('temperature.urls')),
    path('', home, name='home'),
    path('', include('api.urls')),
]
