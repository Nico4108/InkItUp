from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import CustomerView, AppointmentView, saveAppointment, ArtistView, TattooView, saveInkbatch
from . import views

urlpatterns = [
  path('auth/', include('rest_auth.urls')),
  path('Customers/', CustomerView.as_view()),
  path('Appointment/', AppointmentView.as_view()),
  path('createAppointment/', views.saveAppointment),
  path("Artist/",ArtistView.as_view()),
  path("Tatto/", TattooView.as_view()),
  path('createsp/', views.saveInkbatch),
]
