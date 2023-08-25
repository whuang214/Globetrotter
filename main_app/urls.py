from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("itineraries/", views.ItineraryIndex.as_view(), name="index_itinerary"),
    path(
        "itineraries/<int:pk>/",
        views.ItineraryDetail.as_view(),
        name="detail_itinerary",
    ),
    path(
        "itineraries/create/", views.ItineraryCreate.as_view(), name="create_itinerary"
    ),
    path(
        "itineraries/<int:pk>/update/",
        views.ItineraryUpdate.as_view(),
        name="update_itinerary",
    ),
    path(
        "itineraries/<int:pk>/delete/",
        views.ItineraryDelete.as_view(),
        name="delete_itinerary",
    ),
    path(
        "itineraries/<int:itinerary_id>/activities/create/",
        views.ActivityCreate.as_view(),
        name="create_activity",
    ),
    path(
        "itineraries/<int:itinerary_id>/activities/<int:activity_id>/update/",
        views.ActivityUpdate.as_view(),
        name="update_activity",
    ),
    path(
        "itineraries/<int:itinerary_id>/activities/<int:activity_id>/delete/",
        views.ActivityDelete.as_view(),
        name="delete_activity",
    ),
    path(
        "itineraries/<int:itinerary_id>/users/add/",
        views.add_user_to_itinerary,
        name="add_user_to_itinerary",
    ),
    path(
        "itineraries/<int:itinerary_id>/flights/create/",
        views.CreateFlight.as_view(),
        name="create_flight",
    ),
    path(
        "itineraries/<int:itinerary_id>/flights/<int:flight_id>/update/",
        views.UpdateFlight.as_view(),
        name="update_flight",
    ),
]
