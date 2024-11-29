from rest_framework import mixins
from .models import Advertisement, Elevator
from .serializers import AdvertisementSerializer, ElevatorSerializer
from rest_framework import viewsets
from datetime import datetime
from rest_framework.response import Response


class AdvertisementAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def retrieve(self, request, pk=None):
        elevator = self.get_object()
        serializer = ElevatorSerializer(elevator)
        elevator.last_connection = datetime.now()
        elevator.save()
        return Response("success")