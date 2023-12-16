# sulfur/admin.py
from django.contrib import admin
from .models import Tour, Booking, FinancialRecord

admin.site.register(Tour)
admin.site.register(Booking)
admin.site.register(FinancialRecord)
