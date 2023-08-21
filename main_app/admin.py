from django.contrib import admin
from .models import TravelItinerary, Activity, Flight

# Register your models here.

admin.site.register(TravelItinerary)

admin.site.register(Activity)
admin.site.register(Flight)
