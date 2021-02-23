from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Tech
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):

   class Meta:
      model = User
      fields = ("usertype", "username")
      # fields = "__all__"


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ("image", "username", "first_name", "last_name", "email", "location")

class Admin_UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ("image", "username", "usertype", "first_name", "last_name", "email", "location", "groups", "user_permissions", "is_staff", "is_active", "is_superuser")

class TechForm(ModelForm):
    class Meta:
        model = Tech
        fields = ("techname", "price", "digital", "picture")