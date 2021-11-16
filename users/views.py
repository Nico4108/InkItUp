from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

class UserView(APIView):
    def get(self, request):
        Users = User.objects.all()
        return Response({"Users": Users})