from django.urls import path, include

from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.tech_shelter, name='tech_shelter'),
    path('devices', views.devices, name='devices'),
    path('softwares', views.softwares, name='softwares'),
    path('tech_detail/<int:techID>', views.tech_detail, name='tech_detail'),
    
    path('my_tech_shelter', views.my_tech_shelter, name='my_tech_shelter'),
    path('user_tech_shelter/<int:userID>', views.user_tech_shelter, name='user_tech_shelter'),
    path('orders/', views.orders, name="orders"),
    path('ordersrcvd/', views.orders_received, name="orders_received"),
    
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="update_item"),
    path('checkout/', views.checkout, name="checkout"),
    
    path('manage_techs/', views.manageTechs, name="manage_techs"),
    path('manage_my_techs/', views.manageMyTechs, name="manage_my_techs"),
    path('add_tech/', views.addTech, name="add_tech"),    
    path('<int:techID>/update_tech/', views.updateTech, name="update_tech"),
    path('<int:techID>/delete_tech/', views.deleteTech, name="delete_tech"),


    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('users/', views.users, name='users'),
    path('editprofile/<int:userID>', views.editprofile, name='editprofile'),
    path('deleteprofile/<int:userID>', views.deleteprofile, name='deleteprofile'),
    path('deactivateprofile/<int:userID>', views.deactivateprofile, name='deactivateprofile'),
    
]