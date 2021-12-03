from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import CustomerViewCreate, CustomerDetailView, CustomerViewUpdate, CustomerViewDelete, AppointmentViewCreate, AppointmentDetailView, AppointmentViewUpdate, AppointmentViewDelete, ArtistCreateView, TattooView, artiststatsView, tattooparlorstatsView, appointmenttattooView, Ink_Batchnumber_Callback, Register_Tattoo_with_Ink, show_customer, create_appointment_existing_customer
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
  
  path("artist/",ArtistCreateView.as_view()),

  path("tatto/", TattooView.as_view()),

# STORED PROCEDURES
  path('showappointments/<date>/', views.show_appointments, name='show appointmentss'),
  path('updateinkstorage/<str:batchnumber>/', views.Update_ink_storage, name='Update ink storage'),
  path('batchnumbercallback/<str:batchnumber>/', views.Ink_Batchnumber_Callback, name='Ink Batchnumber Callback'),
  path('registertattoo/<int:NewidTattoo>/<str:NewDescription>/<str:NewPlacementOnBody>/<str:NewAppointment_idAppointment>/<str:Inkbatchnumber>/', views.Register_Tattoo_with_Ink, name='Register Tattoo with Ink'),

#MONGODB
  path('mongo/showcustomer/<str:date>/',views.show_customer, name='show customer'),
  path('mongo/createappoinmentec/<int:new_c_id>/<int:new_a_id>/<str:new_datetime>/<int:new_sessionlength>/<int:new_tattooparlorid>/<int:new_artistid>/',views.create_appointment_existing_customer, name='create appointment E C'),

]
