from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm




# inheriting from UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    # adding more fields to the form
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        # add the new fields to the fields list from the parent class
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email")

