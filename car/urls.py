from django.urls import path
from car.views import CarAdsViewSet

urlpatterns = [
    path('', CarAdsViewSet.as_view({'get': 'list', 'post': 'create'}), name='car-list'),  # Replace 'cars/' with the desired URL
]
