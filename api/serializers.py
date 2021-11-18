from rest_framework import serializers
from .models import Customer, Tattooparlor, TattooHasInk, Tattoo, Appointment, Supplier, Artist, artiststats, tattooparlorstats, appointmenttattooview
 
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

class TattooparlorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tattooparlor
        fields = "__all__"

class TattooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tattoo
        fields = "__all__"

class TattooHasInkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooHasInk
        fields = "__all__"

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

# DATABASE VIEWS
class artiststatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = artiststats
        fields = "__all__"


class tattooparlorstatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tattooparlorstats
        fields = "__all__"


class appointmenttattooviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointmenttattooview
        fields = "__all__"
        
        