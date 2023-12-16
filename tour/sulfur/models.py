# sulfur/models.py
from django.db import models
from django.contrib.auth.models import User

class Tour(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transport = models.CharField(max_length=255)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)

class FinancialRecord(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_income = models.BooleanField(default=True)
