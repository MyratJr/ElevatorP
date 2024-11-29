from rest_framework import mixins
from .models import Advertisement
from .serializers import AdvertisementSerializer
from rest_framework.viewsets import GenericViewSet


class AdvertisementAPIView(mixins.ListModelMixin, GenericViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer