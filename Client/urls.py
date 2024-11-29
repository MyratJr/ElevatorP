from django.urls import path
from . import views

urlpatterns = [
    path("client/", views.AdvertisementAPIView.as_view({"get":"list"}), name="client")
]