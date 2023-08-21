from django.shortcuts import render, redirect
from django.urls import reverse_lazy
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
    template_name = "auth/signup_form.html"
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
    template_name = "auth/login_form.html"
    # dont need to specify the form_class b/c it is already specified in the super class
    success_url = reverse_lazy("home")

    # add a title to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Log In"
        return context
