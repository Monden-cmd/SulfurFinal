# sulfur/urls.py
from django.urls import path
from .views import TourListCreateView, TourRetrieveUpdateDestroyView, BookingListCreateView, FinancialRecordListCreateView

urlpatterns = [
    path('tours/', TourListCreateView.as_view(), name='tour-list-create'),
    path('tours/<int:pk>/', TourRetrieveUpdateDestroyView.as_view(), name='tour-detail'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('financial/', FinancialRecordListCreateView.as_view(), name='financial-record-list-create'),

]
