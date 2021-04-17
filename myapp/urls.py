from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.index,name='myapp'),
    path("home",views.home,name='myhome'),
    path("home/<str:pk>",views.cities,name="city")
    
]