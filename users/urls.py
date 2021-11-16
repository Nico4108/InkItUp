from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import UserView

urlpatterns = [
  path('auth/', include('rest_auth.urls')),
  path ('users/', UserView)
]