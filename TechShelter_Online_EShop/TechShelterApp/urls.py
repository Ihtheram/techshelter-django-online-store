from django.urls import path, include

from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.tech_shelter, name='tech_shelter'),

    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('users/', views.users, name='users'),
    path('editprofile/<int:userID>', views.editprofile, name='editprofile'),
    path('deleteprofile/<int:userID>', views.deleteprofile, name='deleteprofile'),
    path('deactivateprofile/<int:userID>', views.deactivateprofile, name='deactivateprofile'),
    
]