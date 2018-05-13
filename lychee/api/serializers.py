from rest_framework import serializers
from temperature.models import Temperature
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature 
        fields = ('temperature', 'max_temp', 'min_temp',)

