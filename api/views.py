from django.shortcuts import render, HttpResponseRedirect, Http404
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import CustomerSerializer, AppointmentSerializer, ArtistSerializer, TattooSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Customer, Appointment, Artist, Tattoo, Ink
from django.db import connection
from django.contrib import messages
from rest_framework import generics

class CustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AppointmentView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


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

class ArtistView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class TattooView(generics.ListCreateAPIView):
    queryset = Tattoo.objects.all()
    serializer_class = TattooSerializer


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