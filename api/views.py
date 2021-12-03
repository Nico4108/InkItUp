from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import CustomerSerializer, AppointmentSerializer, ArtistSerializer, TattooSerializer, artiststatsSerializer, tattooparlorstatsSerializer, appointmenttattooviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Customer, Appointment, Artist, Tattoo, Ink, artiststats, tattooparlorstats, appointmenttattooview
from users.models import User
from django.db import connection
from rest_framework import generics
# from django.db.models.query import QuerySet
from .calls import call_show_appointments, call_Update_ink_storage, call_Ink_Batchnumber_Callback, call_Register_Tattoo_with_Ink, mongo_get_customer, mongo_create_appointment

# pylint: disable=E1101

# CUSTOMER
class CustomerViewCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'cpr'

class CustomerViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'cpr'

class CustomerViewDelete(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'cpr'

# APPOINTMENTS
class AppointmentViewCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# ONLY LOGGED IN USERS APPOINTMENTS
    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.filter(tattooparlor_cvr=self.request.user.Tattooparlor_cvr)
        return queryset

class AppointmentDetailView(generics.RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'cvr'

class AppointmentViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'cvr'

class AppointmentViewDelete(generics.DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'cvr'

class ArtistCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class TattooView(generics.ListCreateAPIView):
    queryset = Tattoo.objects.all()
    serializer_class = TattooSerializer

# DATABASE VIEWS

class artiststatsView(generics.ListAPIView):
    queryset = artiststats.objects.all()
    serializer_class = artiststatsSerializer

class tattooparlorstatsView(generics.ListAPIView):
    queryset = tattooparlorstats.objects.all()
    serializer_class = tattooparlorstatsSerializer

class appointmenttattooView(generics.ListAPIView):
    queryset = appointmenttattooview.objects.all()
    serializer_class = appointmenttattooviewSerializer


# STORED PROCEDURES FUNCTION BASED
def show_appointments(request, date):
    Storedp = call_show_appointments(date)
    return HttpResponse(Storedp, content_type = 'application/json')


def Update_ink_storage(request, batchnumber):
    call_Update_ink_storage(batchnumber)
    return HttpResponse(content_type = 'application/json')


def Ink_Batchnumber_Callback(request, batchnumber):
    Storedp = call_Ink_Batchnumber_Callback(batchnumber)
    return HttpResponse(Storedp, content_type = 'application/json')


def Register_Tattoo_with_Ink(request, NewidTattoo, NewDescription, NewPlacementOnBody, NewAppointment_idAppointment, Inkbatchnumber):
    call_Register_Tattoo_with_Ink(NewidTattoo, NewDescription, NewPlacementOnBody, NewAppointment_idAppointment, Inkbatchnumber)
    return HttpResponse(content_type = 'application/json')

#MONGODB -----------------

def show_customer(request, date):
    action = mongo_get_customer(date)
    return HttpResponse(action, content_type = "application/json")

def create_appointment_existing_customer(request, new_c_id, new_a_id, new_datetime, new_sessionlength, new_tattooparlorid, new_artistid):
    new_appointment = mongo_create_appointment(new_c_id, new_a_id, new_datetime, new_sessionlength, new_tattooparlorid, new_artistid)
    return HttpResponse(new_appointment, content_type = "application/json")