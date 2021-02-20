from django.urls import path, include

from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.tech_shelter, name='tech_shelter'),

    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]