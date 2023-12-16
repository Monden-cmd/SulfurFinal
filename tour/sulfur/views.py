#from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import Tour, Booking, FinancialRecord
from .serializers import TourSerializer, BookingSerializer, FinancialRecordSerializer

class TourListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAuthenticated]

class TourRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAuthenticated]

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Додаємо зв'язок між бронюванням та туром при створенні бронювання
        tour_id = self.request.data.get('tour')
        tour = Tour.objects.get(pk=tour_id)
        serializer.save(tour=tour)

class FinancialRecordListCreateView(generics.ListCreateAPIView):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Додаємо зв'язок між фінансовим записом та туром/бронюванням при створенні запису
        tour_id = self.request.data.get('tour')
        booking_id = self.request.data.get('booking')

        if tour_id:
            tour = Tour.objects.get(pk=tour_id)
            serializer.save(tour=tour)
        elif booking_id:
            booking = Booking.objects.get(pk=booking_id)
            serializer.save(booking=booking)
        else:
            serializer.save()
