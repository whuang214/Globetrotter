from django.db import models
from datetime import date
from datetime import time
from django.contrib.auth.models import User


CATEGORIES = (
    ('S', 'Sightseeing'),
    ('T', 'Things To-Do'),
    ('F', 'Food')
)

# Create your models here.

class TravelItinerary(models.Model):
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField
    location = models.CharField(max_length=100)
    notes = models.TextField()


class Activity(models.Model):
    activity_name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    date_time = models.DateTimeField()
    location = models.CharField(max_length=100)

    #create a travel_itinerary FK bc one itinerary has many activities
    travelItinerary = models.ForeignKey(TravelItinerary, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_category_display()} on {self.date_time}"
    
    class Meta:
        ordering = ['-date_time']

    