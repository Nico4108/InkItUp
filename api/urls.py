from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import CustomerViewCreate, CustomerDetailView, CustomerViewUpdate, CustomerViewDelete, AppointmentViewCreate, AppointmentDetailView, AppointmentViewUpdate, AppointmentViewDelete, saveAppointment, ArtistCreateView, TattooView, saveInkbatch, artiststatsView, tattooparlorstatsView, appointmenttattooView
from . import views

urlpatterns = [
  path('auth/', include('rest_auth.urls')),

  path('customers/', CustomerViewCreate.as_view()),
  path('<cpr>/detailcustomer/', CustomerDetailView.as_view()),
  path('<cpr>/updatecustomer/', CustomerViewUpdate.as_view()),
  path('<cpr>/deletecustomer/', CustomerViewDelete.as_view()),

  path('appointments/', AppointmentViewCreate.as_view()),
  path('<cvr>/detailappointment/', AppointmentDetailView.as_view()),
  path('<cvr>/updateappointment/', AppointmentViewUpdate.as_view()),
  path('<cvr>/deleteappointment/', AppointmentViewDelete.as_view()),
# DATABASE VIEWS
  path('artiststatsview/', artiststatsView.as_view()),
  path('tattooparlorstatsview/', tattooparlorstatsView.as_view()),
  path('appointmenttattooview/', appointmenttattooView.as_view()),

  path('createappointment/', views.saveAppointment),
  
  path("artist/",ArtistCreateView.as_view()),

  path("tatto/", TattooView.as_view()),

  path('createsp/', views.saveInkbatch),
]
