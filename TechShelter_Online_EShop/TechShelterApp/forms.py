from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):

   class Meta:
      model = User
      fields = ("usertype", "username")
      # fields = "__all__"


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("image", "username", "first_name", "last_name", "email", "location")