from django.db import models
from datetime import datetime
from datetime import time
from django.contrib.auth.models import User


CATEGORIES = (("S", "Sightseeing"), ("T", "Things To-Do"), ("F", "Food"))

# user's pk - kwargs={'pk' : self_id}

# Create your models here.


class TravelItinerary(models.Model):
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    hotel = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.id})"


class Activity(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=1, choices=CATEGORIES, default=CATEGORIES[0][0]
    )
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)

    # create a travel_itinerary FK bc one itinerary has many activities
    travelItinerary = models.ForeignKey(TravelItinerary, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_category_display()}"

    class Meta:
        ordering = ["date", "time"]


class Flight(models.Model):
    flight = models.CharField(max_length=100)
    arrival_time = models.TimeField()

    # create a travel_itinerary FK bc one itinerary has many flights
    travelItinerary = models.ForeignKey(TravelItinerary, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"
