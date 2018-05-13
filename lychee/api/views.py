from django.shortcuts import render
from api.serializers import UserSerializer, TemperatureSerializer
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from temperature.models import Temperature

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer


