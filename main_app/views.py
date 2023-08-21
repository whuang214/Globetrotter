from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# models imports
from .models import TravelItinerary

# auth imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# GET request gets the view
# POST request submits the form
class SignUpView(CreateView):
    template_name = "auth/auth_form.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("home")

    # add a title to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sign Up"
        return context


# automatically passes in fields from the form
# fields: username, password
class LoginView(LoginView):
    template_name = "auth/auth_form.html"
    # dont need to specify the form_class b/c it is already specified in the super class
    success_url = reverse_lazy("home")

    # add a title to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Log In"
        return context


# GET request will render the template
class ItineraryIndex(ListView):
    model = TravelItinerary
    template_name = "itineraries/index.html"
    context_object_name = "itineraries"

    # set the queryset to return only the itineraries for the currently logged in user
    def get_queryset(self):
        # Get the user from the URL parameter or session
        user = self.request.user

        # Filter items based on the user
        queryset = TravelItinerary.objects.filter(user=user)
        return queryset


class ItineraryDetail(DetailView):
    model = TravelItinerary
    template_name = "itineraries/detail.html"
    context_object_name = "itinerary"


class ItineraryCreate(CreateView):
    model = TravelItinerary
    template_name = "itineraries/create.html"
    fields = "__all__"
    success_url = reverse_lazy("index")

    # TODO - set the user field to the currently logged in user
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


class ItineraryUpdate(UpdateView):
    model = TravelItinerary
    template_name = "itineraries/update.html"
    fields = "__all__"
    success_url = reverse_lazy("index")


class ItineraryDelete(DeleteView):
    model = TravelItinerary
    template_name = "itineraries/delete.html"
    success_url = reverse_lazy("index")
