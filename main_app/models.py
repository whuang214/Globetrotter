from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class TravelItinerary(models.Model):
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField
    location = models.CharField(max_length=100)
    notes = models.TextField()