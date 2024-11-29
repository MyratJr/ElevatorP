from rest_framework import mixins
from .models import Advertisement, Elevator
from .serializers import AdvertisementSerializer, ElevatorSerializer
from rest_framework import viewsets, generics
from datetime import datetime
from rest_framework.response import Response


class AdvertisementAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()

    def retrieve(self, request, pk=None):
        elevator = self.get_object()
        elevator.last_connection = datetime.now()
        elevator.save()
        return Response("success")
    

class AdvertisementByElevatorAPIView(generics.ListAPIView):

    def get_queryset(self):
        elevator_id = self.kwargs['elevator_id']
        elevator = Elevator.objects.get(pk=elevator_id)
        group_id = elevator.parent_id
        return Advertisement.objects.filter(parent_id=group_id)