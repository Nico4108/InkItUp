from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import CustomerSerializer, AppointmentSerializer, ArtistSerializer, TattooSerializer, artiststatsSerializer, tattooparlorstatsSerializer, appointmenttattooviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Customer, Appointment, Artist, Tattoo, Ink, artiststats, tattooparlorstats, appointmenttattooview
from django.db import connection
from django.contrib import messages
from rest_framework import generics

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


@csrf_exempt
def saveAppointment(request):
        if request.method == 'POST':
            if request.POST.get('idAppointment') and request.POST.get('DateTime') and request.POST.get('SessionLenght') and request.POST.get('Customer_CPR') and request.POST.get('Tattooparlor_CVR') and request.POST.get('Artist_CPR'):
                save=Appointment()
                save.idAppointment=request.POST.get('idAppointment')
                save.DateTime=request.POST.get('DateTime')
                save.SessionLenght=request.POST.get('SessionLenght')
                save.Customer_CPR=request.POST.get('Customer_CPR')
                save.Tattooparlor_CVR=request.POST.get('Tattooparlor_CVR')
                save.Artist_CPR=request.POST.get('Artist_CPR')
                cursor=connection.cursor()
                cursor.execute("call CreateAppointment('"+save.idAppointment+"', '"+save.DateTime+"', '"+save.SessionLenght+"', '"+save.Customer_CPR+"', '"+save.Tattooparlor_CVR+"', '"+save.Artist_CPR+"')")
                messages.success(request, "The Apointment "+save.idAppointment+"")
                data = JSONParser().parse(request)
                serializer =AppointmentSerializer(data = data)
                return HttpResponse(serializer.data,status =400)


@csrf_exempt
def saveInkbatch(request):
        if request.method == 'POST':
            if request.POST.get('batchnumber'):
                save=Ink()
                save.batchnumber=request.POST.get('batchnumber')
                cursor=connection.cursor()
                cursor.execute("call InkItUp.InkBatchNumberCallBackk('"+save.batchnumber+"')")
                messages.success(request, "The batchnumber "+save.batchnumber+"")
                return HttpResponse(request, content_type = 'application/json')