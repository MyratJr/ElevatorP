from django.urls import path
from . import views

urlpatterns = [
    path("list-advertisements/", views.AdvertisementAPIView.as_view({"get":"list"}), name="advertisements"), 
    path('tablet-update-connection/<int:pk>/', views.ElevatorViewSet.as_view({'get': 'retrieve'}), name='tablet_connection_update'),
    path('elevator-advertisements/<int:elevator_id>', views.AdvertisementByElevatorAPIView.as_view()),
]