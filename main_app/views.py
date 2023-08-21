from django.shortcuts import render
from django.views.generic import ListView
from .models import TravelItinerary


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# GET request will render the template
class ItineraryIndex(ListView):
    model = TravelItinerary
    template_name = 'itineraries/index.html'
    context_object_name = 'itineraries'
    
    # set the queryset to return only the itineraries for the currently logged in user
    def get_queryset(self): 
        # Get the user from the URL parameter or session
        user = self.request.user
        
        # Filter items based on the user
        queryset = TravelItinerary.objects.filter(user=user)
        return queryset