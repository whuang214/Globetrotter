from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# models imports
from .models import TravelItinerary, Activity
from .forms import CustomUserCreationForm

# auth imports
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# GET request gets the view
# POST request submits the form
class SignUpView(CreateView):
    template_name = "auth/signup_form.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")

    # add a title to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sign Up"
        return context

    def form_valid(self, form):
        # Save the form and create the user
        response = super().form_valid(form)

        # Log in the user after signing up
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        if user is not None:
            login(self.request, user)

        return response


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


class LogoutView(LogoutView):
    template_name = "auth/logout_form.html"
    success_url = reverse_lazy("home")


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
        queryset = TravelItinerary.objects.filter(users=user)
        return queryset


class ItineraryDetail(DetailView):
    model = TravelItinerary
    template_name = "itineraries/detail.html"
    context_object_name = "itinerary"


class ItineraryCreate(CreateView):
    model = TravelItinerary
    template_name = "itineraries/create.html"
    fields = ["title", "start_date", "end_date", "location"]
    success_url = reverse_lazy("index_itinerary")

    # override the get_form method to add the datepicker attribute to the date fields
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        # Adding attributes to the end_date widget using attrs
        form.fields["title"].widget.attrs.update(
            {
                "placeholder": "Enter Title",
                "class": "form-control",
            }
        )
        form.fields["start_date"].widget.attrs.update(
            {
                "placeholder": "Enter Start Date",
                "data-provide": "datepicker",
                "class": "form-control",
            }
        )

        form.fields["end_date"].widget.attrs.update(
            {
                "placeholder": "Enter End Date",
                "data-provide": "datepicker",
                "class": "form-control",
            }
        )
        form.fields["location"].widget.attrs.update(
            {
                "placeholder": "Enter Location",
                "class": "form-control",
            }
        )
        return form

    # override the form_valid method to add the user to the itinerary
    def form_valid(self, form):
        # doesnt work because user attribute does not exist on the itinerary model.
        # The itinerary model has a users (array) not a user (single user)
        # form.instance.user = self.request.user

        # save the form and get the itinerary object
        itinerary = form.save(commit=False)
        itinerary.save()
        # add user to array of users in the itinerary
        itinerary.users.add(self.request.user)

        return super().form_valid(form)


class ItineraryUpdate(UpdateView):
    model = TravelItinerary
    template_name = "itineraries/update.html"
    fields = "__all__"
    success_url = reverse_lazy("index_itinerary")


class ItineraryDelete(DeleteView):
    model = TravelItinerary
    template_name = "itineraries/delete.html"
    context_object_name = "itinerary"
    success_url = reverse_lazy("index_itinerary")


class ActivityCreate(CreateView):
    model = Activity
    template_name = "activities/create.html"
    fields = ["name", "category", "date_time", "location"]
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["date_time"].widget.attrs.update(
            {
                "data-provide": "datepicker",
                "class": "datepicker form-control datetimepicker-input",
            }
        )
        return form
    def form_valid(self, form):
        # Get the itinerary_pk from the URL
        itinerary_id = self.kwargs["itinerary_id"]

        # Get the travel itinerary instance
        travel_itinerary = get_object_or_404(TravelItinerary, pk=itinerary_id)

        # Set the travel itinerary for the activity
        activity = form.save(commit=False)
        activity.travelItinerary = travel_itinerary
        activity.save()

        return redirect("detail_itinerary", pk=itinerary_id)
        


class ActivityUpdate(UpdateView):
    model = Activity
    template_name = "activities/update.html"
    context_object_name = "activity"
    fields = "__all__"

    def get_object(self, queryset=None):
        itinerary_id = self.kwargs.get("itinerary_id")
        activity_id = self.kwargs.get("activity_id")
        activity = get_object_or_404(
            Activity, id=activity_id, travelItinerary_id=itinerary_id
        )
        return activity

    def get_success_url(self):
        itinerary_id = self.kwargs.get("itinerary_id")
        return reverse("detail_itinerary", kwargs={"pk": itinerary_id})


class ActivityDelete(DeleteView):
    model = Activity
    template_name = "activities/delete.html"
    context_object_name = "activity"

    def get_object(self, queryset=None):
        itinerary_id = self.kwargs.get("itinerary_id")
        activity_id = self.kwargs.get("activity_id")
        activity = get_object_or_404(
            Activity, id=activity_id, travelItinerary_id=itinerary_id
        )
        return activity

    def get_success_url(self):
        itinerary_id = self.kwargs.get("itinerary_id")
        return reverse("detail_itinerary", kwargs={"pk": itinerary_id})
