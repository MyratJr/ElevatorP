from django.urls import path
from . import views

urlpatterns = [
    path("advertisements/", views.AdvertisementAPIView.as_view({"get":"list"}), name="advertisements")
]