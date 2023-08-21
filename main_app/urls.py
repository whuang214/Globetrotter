from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("itineraries/", views.ItineraryIndex.as_view(), name="index"),
    path("itineraries/<int:pk>/", views.ItineraryDetail.as_view(), name="detail"),
    path("itineraries/create/", views.ItineraryCreate.as_view(), name="create"),
    path(
        "itineraries/<int:pk>/update/", views.ItineraryUpdate.as_view(), name="update"
    ),
    path(
        "itineraries/<int:pk>/delete/", views.ItineraryDelete.as_view(), name="delete"
    ),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
