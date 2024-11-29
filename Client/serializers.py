from rest_framework import serializers
from .models import Advertisement, Elevator


class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ["id", "title", "description", "media", "filetype", "duration"]


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ["id", "name", ]