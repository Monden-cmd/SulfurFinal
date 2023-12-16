# sulfur/serializers.py
from rest_framework import serializers
from .models import Tour, Booking, FinancialRecord

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'place', 'date', 'price', 'transport']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'tour', 'user', 'date']

class FinancialRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialRecord
        fields = ['id', 'tour', 'booking', 'income', 'expense', 'date']
