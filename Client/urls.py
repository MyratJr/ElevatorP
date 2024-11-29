from django.urls import path
from . import views

urlpatterns = [
    path("advertisements/", views.AdvertisementAPIView.as_view({"get":"list"}), name="advertisements"), 
    path('tablet-update-connection/<int:pk>/', views.ElevatorViewSet.as_view({'get': 'retrieve'}), name='tablet_connection_update'),
]