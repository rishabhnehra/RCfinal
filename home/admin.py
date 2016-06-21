from django.contrib import admin
from .models import Booking, DisabledDates
from .forms import BookingForm

class BookingAdmin(admin.ModelAdmin):
	list_display = ["email", "timestamp", "first_name", "last_name", "mobile_number","ip_address"]
	list_filter = ["timestamp"]
	search_fields = ["email", "first_name", "last_name", "mobile_number", "message"]
	

# Register your models here.
admin.site.register(Booking, BookingAdmin)
admin.site.register(DisabledDates)