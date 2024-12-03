from rest_framework import mixins
from .models import Advertisement, Elevator
from .serializers import AdvertisementSerializer
from rest_framework import viewsets, generics
from datetime import datetime


class AdvertisementAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Advertisement.objects.all()
    for i in Elevator.objects.all():
        i.last_connection = datetime.now()
        print(i.last_connection)
        i.save()
    serializer_class = AdvertisementSerializer


class AdvertisementByElevatorAPIView(generics.ListAPIView):
    serializer_class = AdvertisementSerializer

    def get_queryset(self):
        elevator_id = self.kwargs['elevator_id']
        elevator = Elevator.objects.get(pk=elevator_id)
        elevator.last_connection = datetime.now()
        elevator.save()
        group_id = elevator.parent_id
        return Advertisement.objects.filter(parent_id=group_id)