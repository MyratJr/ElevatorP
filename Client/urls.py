from django.urls import path
from . import views

urlpatterns = [
    path("list-advertisements/", views.AdvertisementAPIView.as_view({"get":"list"}), name="advertisements"), 
    path('elevator-advertisements/<int:elevator_id>', views.AdvertisementByElevatorAPIView.as_view()),
]